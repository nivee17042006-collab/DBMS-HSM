from __future__ import annotations

import os
import re
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote_plus

from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import StaticPool


app = Flask(__name__)
app.config["SECRET_KEY"] = "hospital-management-demo"
database_url = os.getenv("DATABASE_URL")
mysql_host = os.getenv("MYSQL_HOST")
using_mysql = bool(database_url or mysql_host)

if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
elif mysql_host:
    mysql_user = os.getenv("MYSQL_USER", "root")
    mysql_password = quote_plus(os.getenv("MYSQL_PASSWORD", ""))
    mysql_port = os.getenv("MYSQL_PORT", "3306")
    mysql_database = os.getenv("MYSQL_DATABASE", "hms_batch4")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{mysql_user}:{mysql_password}@"
        f"{mysql_host}:{mysql_port}/{mysql_database}"
    )
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "connect_args": {"check_same_thread": False},
        "poolclass": StaticPool,
    }
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

SQL_IMPORT_PATH =Path(__file__).resolve().parent / "hms_batch4_dataset.sql"
USER_INSERT_RE = re.compile(
    r"INSERT INTO users \(username, password, role\) VALUES \('([^']*)', '([^']*)', '([^']*)'\);"
)
ACCESS_INSERT_RE = re.compile(
    r"INSERT INTO access_layers \(username, biothumb_id, department\) VALUES \('([^']*)', '([^']*)', '([^']*)'\);"
)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    condition = db.Column(db.String(120), nullable=False)
    ward = db.Column(db.String(60), nullable=False)
    admission_type = db.Column(db.String(40), nullable=False)
    registered_by = db.Column(db.String(40), nullable=False)
    emergency_case = db.Column(db.Boolean, nullable=False, default=False)
    admitted_on = db.Column(db.Date, nullable=False, default=date.today)


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(80), nullable=False)
    availability = db.Column(db.String(80), nullable=False)
    assigned_ward = db.Column(db.String(60), nullable=False)


class StaffUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(40), nullable=False)
    department = db.Column(db.String(80), nullable=False)
    login_id = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    security_pin = db.Column(db.String(80), nullable=False)
    two_factor_mode = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(30), nullable=False, default="Active")


class WardAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(120), nullable=False)
    doctor_name = db.Column(db.String(120), nullable=False)
    nurse_name = db.Column(db.String(120), nullable=False)
    ward_name = db.Column(db.String(60), nullable=False)
    room_number = db.Column(db.String(20), nullable=False)
    schedule = db.Column(db.String(80), nullable=False)


class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(120), nullable=False)
    doctor_name = db.Column(db.String(120), nullable=False)
    nurse_name = db.Column(db.String(120), nullable=False)
    medicines = db.Column(db.String(255), nullable=False)
    dosage = db.Column(db.String(255), nullable=False)
    prescribed_on = db.Column(db.Date, nullable=False, default=date.today)


class PharmacyStock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(120), nullable=False)
    stock_in = db.Column(db.Integer, nullable=False, default=0)
    stock_out = db.Column(db.Integer, nullable=False, default=0)
    balance_units = db.Column(db.Integer, nullable=False)
    prescribed_to = db.Column(db.String(120), nullable=False)
    prescribed_by = db.Column(db.String(120), nullable=False)
    approval_status = db.Column(db.String(40), nullable=False)
    order_status = db.Column(db.String(60), nullable=False)


class IotBandMonitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(120), nullable=False)
    band_code = db.Column(db.String(60), nullable=False)
    anomaly = db.Column(db.String(120), nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    spo2 = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    monitored_by = db.Column(db.String(80), nullable=False)
    last_sync = db.Column(db.String(60), nullable=False)


class InfantSecurity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    infant_name = db.Column(db.String(120), nullable=False)
    mother_name = db.Column(db.String(120), nullable=False)
    pair_code = db.Column(db.String(60), nullable=False)
    authorized_members = db.Column(db.String(255), nullable=False)
    alarm_status = db.Column(db.String(120), nullable=False)
    alert_targets = db.Column(db.String(255), nullable=False)
    technical_team = db.Column(db.String(120), nullable=False)


def prettify_username(username: str, role: str) -> str:
    if username == "admin_root":
        return "Admin Root"
    pieces = [piece for piece in username.split("_") if piece]
    if role.lower() == "doctor" and pieces and pieces[0] == "dr":
        return "Dr. " + " ".join(part.capitalize() for part in pieces[1:])
    if role.lower() == "nurse" and pieces and pieces[0] == "nurse":
        return "Nurse " + " ".join(part.capitalize() for part in pieces[1:])
    if pieces and pieces[0] == "staff":
        return " ".join(part.capitalize() for part in pieces[1:])
    if pieces and pieces[0] == "clean":
        return "Cleaner " + " ".join(part.capitalize() for part in pieces[1:])
    return " ".join(part.capitalize() for part in pieces)


def parse_staff_sql() -> list[dict]:
    if not SQL_IMPORT_PATH.exists():
        return []

    user_rows: dict[str, dict] = {}
    access_rows: dict[str, dict] = {}

    for line in SQL_IMPORT_PATH.read_text(encoding="utf-8").splitlines():
        user_match = USER_INSERT_RE.search(line)
        if user_match:
            username, password, role = user_match.groups()
            if username == "---":
                continue
            user_rows[username] = {"password": password, "role": role}
            continue

        access_match = ACCESS_INSERT_RE.search(line)
        if access_match:
            username, biothumb_id, department = access_match.groups()
            if username == "---":
                continue
            access_rows[username] = {
                "security_pin": biothumb_id,
                "department": department,
            }

    records = []
    for username, user_row in user_rows.items():
        access_row = access_rows.get(
            username, {"security_pin": "UNKNOWN", "department": "General"}
        )
        records.append(
            {
                "full_name": prettify_username(username, user_row["role"]),
                "role": user_row["role"],
                "department": access_row["department"],
                "login_id": username,
                "password": user_row["password"],
                "security_pin": access_row["security_pin"],
                "two_factor_mode": "Password + Biometric Code",
                "status": "Active",
            }
        )
    return records


def seed_data() -> None:
    if Patient.query.first():
        return

    imported_staff = parse_staff_sql()
    doctor_rows = [row for row in imported_staff if row["role"] == "Doctor"]

    db.session.add_all(
        [
            Patient(
                full_name="Kaviya Raj",
                age=29,
                gender="Female",
                phone="9876543210",
                condition="Post-surgery recovery",
                ward="Ward A",
                admission_type="Inpatient",
                registered_by="Admin",
                emergency_case=False,
                admitted_on=date(2026, 4, 14),
            ),
            Patient(
                full_name="Arjun Kumar",
                age=41,
                gender="Male",
                phone="9789012345",
                condition="Cardiac observation",
                ward="ICU 2",
                admission_type="Emergency",
                registered_by="Receptionist",
                emergency_case=True,
                admitted_on=date(2026, 4, 15),
            ),
            WardAssignment(
                patient_name="Arjun Kumar",
                doctor_name="Dr. Arjun",
                nurse_name="Nurse Deepa",
                ward_name="ICU 2",
                room_number="ICU-08",
                schedule="Vitals every 2 hours",
            ),
            WardAssignment(
                patient_name="Kaviya Raj",
                doctor_name="Dr. Sneha",
                nurse_name="Nurse Kavi",
                ward_name="Ward A",
                room_number="A-12",
                schedule="Morning and evening rounds",
            ),
            Prescription(
                patient_name="Arjun Kumar",
                doctor_name="Dr. Arjun",
                nurse_name="Nurse Deepa",
                medicines="Aspirin, Atorvastatin",
                dosage="1-0-1 for 5 days",
                prescribed_on=date(2026, 4, 15),
            ),
            Prescription(
                patient_name="Kaviya Raj",
                doctor_name="Dr. Sneha",
                nurse_name="Nurse Kavi",
                medicines="Paracetamol, Cefixime",
                dosage="1-1-1 after food",
                prescribed_on=date(2026, 4, 16),
            ),
            PharmacyStock(
                medicine_name="Aspirin",
                stock_in=100,
                stock_out=24,
                balance_units=76,
                prescribed_to="Arjun Kumar",
                prescribed_by="Dr. Arjun",
                approval_status="Approved by Admin",
                order_status="In stock",
            ),
            PharmacyStock(
                medicine_name="Infant Vitamin Drops",
                stock_in=20,
                stock_out=18,
                balance_units=2,
                prescribed_to="NICU",
                prescribed_by="Dr. Sneha",
                approval_status="Awaiting Admin Approval",
                order_status="Restock requested",
            ),
            IotBandMonitor(
                patient_name="Arjun Kumar",
                band_code="IOT-ARJ-2201",
                anomaly="Irregular heart rate detected",
                heart_rate=122,
                spo2=93,
                temperature=99.4,
                monitored_by="Staff Karthik",
                last_sync="16 Apr 2026, 08:45 AM",
            ),
            IotBandMonitor(
                patient_name="Kaviya Raj",
                band_code="IOT-KAV-1140",
                anomaly="No anomaly",
                heart_rate=82,
                spo2=98,
                temperature=98.4,
                monitored_by="Staff Karthik",
                last_sync="16 Apr 2026, 08:50 AM",
            ),
            InfantSecurity(
                infant_name="Baby Diya",
                mother_name="Meena S",
                pair_code="MOM-INF-9088",
                authorized_members="Mother, Dr. Sneha, Nurse Kavi",
                alarm_status="Protected",
                alert_targets="Reception, Doctor, Nurse",
                technical_team="Staff Karthik",
            ),
            InfantSecurity(
                infant_name="Baby Keshav",
                mother_name="Anu K",
                pair_code="MOM-INF-9011",
                authorized_members="Mother, NICU doctor, Assigned nurse",
                alarm_status="Band tamper alert test enabled",
                alert_targets="Reception, NICU Desk, Nurse Station",
                technical_team="Staff Karthik",
            ),
        ]
    )
    db.session.add_all(
        [
            Doctor(
                full_name=row["full_name"],
                department=row["department"],
                availability="Mon-Sat, 9 AM - 5 PM",
                assigned_ward=row["department"],
            )
            for row in doctor_rows
        ]
    )
    db.session.add_all([StaffUser(**row) for row in imported_staff])
    db.session.commit()


def get_admin_snapshot() -> dict:
    return {
        "patients": Patient.query.count(),
        "doctors": Doctor.query.count(),
        "staff": StaffUser.query.count(),
        "critical_alerts": IotBandMonitor.query.filter(
            IotBandMonitor.anomaly != "No anomaly"
        ).count(),
        "emergency_cases": Patient.query.filter_by(emergency_case=True).count(),
        "awaiting_restock": PharmacyStock.query.filter(
            PharmacyStock.approval_status != "Approved by Admin"
        ).count(),
    }


@app.route("/", methods=["GET"])
def home():
    return render_template(
        "home.html",
        snapshot=get_admin_snapshot(),
        recent_patients=Patient.query.order_by(Patient.admitted_on.desc()).limit(4).all(),
    )


@app.route("/staff-login", methods=["POST"])
def staff_login():
    role = request.form["role"]
    login_id = request.form["login_id"]
    layer_one = request.form["layer_one"]
    layer_two = request.form["layer_two"]

    if not layer_one or not layer_two:
        flash("Two-layer protection needs both password and security code.")
        return redirect(url_for("home"))

    user = StaffUser.query.filter_by(login_id=login_id).first()
    if user is None:
        flash("Login ID not found.")
        return redirect(url_for("home"))

    if user.password != layer_one or user.security_pin != layer_two:
        flash("Invalid password or security code.")
        return redirect(url_for("home"))

    role_valid = (
        (role == "Admin" and user.role == "Admin")
        or (role == "Doctor" and user.role == "Doctor")
        or (role == "Nurse" and user.role == "Nurse")
        or (role == "Staff" and user.role == "Staff")
        or (role == "Pharmacy" and "Pharmacy" in user.department)
        or (role == "IoT" and user.department == "IT Support / AI")
    )
    if not role_valid:
        flash("This account is not allowed for the selected portal.")
        return redirect(url_for("home"))

    route_map = {
        "Admin": "admin_dashboard",
        "Doctor": "doctor_portal",
        "Nurse": "nurse_portal",
        "Staff": "staff_portal",
        "Pharmacy": "pharmacy_portal",
        "IoT": "iot_portal",
    }
    session["login_id"] = user.login_id
    flash(f"{role} login accepted for {user.full_name}.")
    return redirect(url_for(route_map[role]))


@app.route("/patient-register", methods=["POST"])
def patient_register():
    patient = Patient(
        full_name=request.form["full_name"],
        age=int(request.form["age"]),
        gender=request.form["gender"],
        phone=request.form["phone"],
        condition=request.form["condition"],
        ward=request.form["ward"],
        admission_type=request.form["admission_type"],
        registered_by=request.form["registered_by"],
        emergency_case=request.form.get("emergency_case") == "yes",
        admitted_on=datetime.strptime(request.form["admitted_on"], "%Y-%m-%d").date(),
    )
    db.session.add(patient)
    db.session.commit()
    flash("Patient registration submitted successfully.")
    return redirect(url_for("home"))


@app.route("/admin/dashboard")
def admin_dashboard():
    pharmacy_waiting = PharmacyStock.query.filter(
        PharmacyStock.approval_status != "Approved by Admin"
    ).all()
    emergency_patients = Patient.query.filter_by(emergency_case=True).all()
    return render_template(
        "admin_dashboard.html",
        snapshot=get_admin_snapshot(),
        pharmacy_waiting=pharmacy_waiting,
        emergency_patients=emergency_patients,
    )


def render_role_portal(title: str, subtitle: str, highlight_label: str, highlight_value: str, sections: list[dict]):
    return render_template(
        "role_portal.html",
        title=title,
        subtitle=subtitle,
        highlight_label=highlight_label,
        highlight_value=highlight_value,
        sections=sections,
    )


@app.route("/doctor/portal")
def doctor_portal():
    return render_role_portal(
        "Doctor Portal",
        "Patient records, ward scheduling, patient monitoring, and medicine prescriptions.",
        "Doctor access",
        f"{Prescription.query.count()} active prescriptions",
        [
            {
                "title": "Patient Records",
                "columns": ["Patient", "Condition", "Ward", "Registered By"],
                "rows": [
                    [p.full_name, p.condition, p.ward, p.registered_by]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).all()
                ],
            },
            {
                "title": "Ward And Patient Schedule",
                "columns": ["Patient", "Doctor", "Nurse", "Ward", "Schedule"],
                "rows": [
                    [w.patient_name, w.doctor_name, w.nurse_name, w.ward_name, w.schedule]
                    for w in WardAssignment.query.order_by(WardAssignment.ward_name).all()
                ],
            },
            {
                "title": "Pharmacy Prescription Flow",
                "columns": ["Patient", "Doctor", "Medicines", "Dosage"],
                "rows": [
                    [p.patient_name, p.doctor_name, p.medicines, p.dosage]
                    for p in Prescription.query.order_by(Prescription.prescribed_on.desc()).all()
                ],
            },
        ],
    )


@app.route("/nurse/portal")
def nurse_portal():
    return render_role_portal(
        "Nurse Portal",
        "Patient details and doctor-prescribed medicine details for bedside care.",
        "Nursing load",
        f"{WardAssignment.query.count()} active ward assignments",
        [
            {
                "title": "Patient Details",
                "columns": ["Patient", "Age", "Condition", "Ward", "Emergency"],
                "rows": [
                    [p.full_name, str(p.age), p.condition, p.ward, "Yes" if p.emergency_case else "No"]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).all()
                ],
            },
            {
                "title": "Doctor Prescribed Details",
                "columns": ["Patient", "Doctor", "Nurse", "Medicines", "Dosage"],
                "rows": [
                    [p.patient_name, p.doctor_name, p.nurse_name, p.medicines, p.dosage]
                    for p in Prescription.query.order_by(Prescription.prescribed_on.desc()).all()
                ],
            },
        ],
    )


@app.route("/staff/portal")
def staff_portal():
    login_id = session.get("login_id")
    user = StaffUser.query.filter_by(login_id=login_id).first() if login_id else None

    if not user:
        flash("Please log in first.")
        return redirect(url_for("home"))

    department = user.department

    if department == "Pharmacy Manager":
        return redirect(url_for("pharmacy_portal"))
    elif department == "IT Support / AI":
        return redirect(url_for("iot_portal"))
    elif department == "Receptionist" or department == "Reception/Triage":
        sections = [
            {
                "title": "Recent Patient Registrations",
                "columns": ["Patient", "Age", "Condition", "Admission Type", "Ward"],
                "rows": [
                    [p.full_name, str(p.age), p.condition, p.admission_type, p.ward]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).limit(10).all()
                ],
            },
            {
                "title": "Emergency Patients",
                "columns": ["Patient", "Condition", "Ward", "Registered By"],
                "rows": [
                    [p.full_name, p.condition, p.ward, p.registered_by]
                    for p in Patient.query.filter_by(emergency_case=True).order_by(Patient.admitted_on.desc()).all()
                ],
            },
            {
                "title": "All Ward Assignments",
                "columns": ["Patient", "Doctor", "Nurse", "Ward"],
                "rows": [
                    [w.patient_name, w.doctor_name, w.nurse_name, w.ward_name]
                    for w in WardAssignment.query.order_by(WardAssignment.ward_name).all()
                ],
            }
        ]
        subtitle = "Manage patient intake, emergency records, and view ward locations."
    elif department.startswith("Cleaning"):
        assigned_ward = department.replace("Cleaning - ", "")
        sections = [
            {
                "title": f"Rooms to Clean ({assigned_ward})",
                "columns": ["Patient", "Ward", "Room Number", "Schedule"],
                "rows": [
                    [w.patient_name, w.ward_name, w.room_number, w.schedule]
                    for w in WardAssignment.query.filter(WardAssignment.ward_name.contains(assigned_ward)).all()
                ],
            },
            {
                "title": "All Active Patients",
                "columns": ["Patient", "Ward", "Admission Date"],
                "rows": [
                    [p.full_name, p.ward, p.admitted_on.strftime("%d %b %Y")]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).all()
                ],
            }
        ]
        subtitle = f"Cleaning schedules and occupied rooms for {assigned_ward}."
    elif department == "Billing Clerk":
        sections = [
            {
                "title": "Patient Overview for Billing",
                "columns": ["Patient", "Ward", "Admission Type", "Emergency"],
                "rows": [
                    [p.full_name, p.ward, p.admission_type, "Yes" if p.emergency_case else "No"]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).all()
                ],
            },
            {
                "title": "Pharmacy Usage",
                "columns": ["Medicine", "Patient", "Doctor"],
                "rows": [
                    [m.medicine_name, m.prescribed_to, m.prescribed_by]
                    for m in PharmacyStock.query.filter(PharmacyStock.prescribed_to != "None").all()
                ],
            }
        ]
        subtitle = "Patient and pharmacy details for preparing billing records."
    elif department == "Lab Technician":
        sections = [
            {
                "title": "Patient Conditions",
                "columns": ["Patient", "Condition", "Ward"],
                "rows": [
                    [p.full_name, p.condition, p.ward]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).all()
                ],
            },
            {
                "title": "Active Prescriptions",
                "columns": ["Patient", "Doctor", "Medicines"],
                "rows": [
                    [pr.patient_name, pr.doctor_name, pr.medicines]
                    for pr in Prescription.query.order_by(Prescription.prescribed_on.desc()).all()
                ],
            }
        ]
        subtitle = "Patient diagnostics and active prescriptions for lab coordination."
    elif department == "Security Head":
        sections = [
            {
                "title": "Infant Security Alerts",
                "columns": ["Infant", "Mother", "Alarm Status", "Alert Targets"],
                "rows": [
                    [i.infant_name, i.mother_name, i.alarm_status, i.alert_targets]
                    for i in InfantSecurity.query.order_by(InfantSecurity.infant_name).all()
                ],
            },
            {
                "title": "Emergency Cases",
                "columns": ["Patient", "Condition", "Ward", "Registered By"],
                "rows": [
                    [p.full_name, p.condition, p.ward, p.registered_by]
                    for p in Patient.query.filter_by(emergency_case=True).order_by(Patient.admitted_on.desc()).all()
                ],
            },
            {
                "title": "IoT Alerts",
                "columns": ["Patient", "Band Code", "Anomaly", "Last Sync"],
                "rows": [
                    [r.patient_name, r.band_code, r.anomaly, r.last_sync]
                    for r in IotBandMonitor.query.filter(IotBandMonitor.anomaly != "No anomaly").all()
                ],
            },
        ]
        subtitle = "Security monitoring for emergency movement, infant protection, and active patient alerts."
    elif department == "HR Coordinator":
        sections = [
            {
                "title": "Hospital Staff Directory",
                "columns": ["Name", "Role", "Department", "Status"],
                "rows": [
                    [s.full_name, s.role, s.department, s.status]
                    for s in StaffUser.query.order_by(StaffUser.department.asc()).all()
                ],
            },
            {
                "title": "Two-Layer Access Modes",
                "columns": ["Name", "Login ID", "Access Mode"],
                "rows": [
                    [s.full_name, s.login_id, s.two_factor_mode]
                    for s in StaffUser.query.order_by(StaffUser.login_id.asc()).all()
                ],
            },
        ]
        subtitle = "Human resources view of staff records, login methods, and active departments."
    elif department == "Medical Records":
        sections = [
            {
                "title": "Patient Master Records",
                "columns": ["Patient", "Age", "Condition", "Ward", "Admission Type"],
                "rows": [
                    [p.full_name, str(p.age), p.condition, p.ward, p.admission_type]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).all()
                ],
            },
            {
                "title": "Prescription Archive",
                "columns": ["Patient", "Doctor", "Medicines", "Prescribed On"],
                "rows": [
                    [pr.patient_name, pr.doctor_name, pr.medicines, pr.prescribed_on.strftime("%d %b %Y")]
                    for pr in Prescription.query.order_by(Prescription.prescribed_on.desc()).all()
                ],
            },
            {
                "title": "Ward Assignment Records",
                "columns": ["Patient", "Ward", "Room", "Doctor", "Nurse"],
                "rows": [
                    [w.patient_name, w.ward_name, w.room_number, w.doctor_name, w.nurse_name]
                    for w in WardAssignment.query.order_by(WardAssignment.ward_name.asc()).all()
                ],
            },
        ]
        subtitle = "Central medical records view for patient files, prescriptions, and ward history."
    elif department == "Maintenance":
        sections = [
            {
                "title": "Occupied Wards",
                "columns": ["Patient", "Ward", "Room Number", "Schedule"],
                "rows": [
                    [w.patient_name, w.ward_name, w.room_number, w.schedule]
                    for w in WardAssignment.query.order_by(WardAssignment.ward_name.asc()).all()
                ],
            },
            {
                "title": "Facility Priority Areas",
                "columns": ["Area", "Reason"],
                "rows": [
                    ["ICU 2", "Critical monitoring equipment in active use"],
                    ["Ward A", "Post-surgery patient recovery support"],
                    ["NICU", "Infant security and monitored access"],
                    ["Pharmacy", "Low-stock medicine storage and restock flow"],
                ],
            },
        ]
        subtitle = "Maintenance overview of occupied wards and high-priority facility areas."
    elif department == "Cafeteria Admin":
        sections = [
            {
                "title": "Patient Meal Coordination",
                "columns": ["Patient", "Ward", "Condition", "Admission Type"],
                "rows": [
                    [p.full_name, p.ward, p.condition, p.admission_type]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).all()
                ],
            },
            {
                "title": "Staff Coverage By Department",
                "columns": ["Name", "Department", "Role"],
                "rows": [
                    [s.full_name, s.department, s.role]
                    for s in StaffUser.query.order_by(StaffUser.department.asc()).all()
                ],
            },
        ]
        subtitle = "Cafeteria planning view for inpatient meals and department support coverage."
    else:
        # Default fallback for other staff
        sections = [
            {
                "title": "Staff Directory",
                "columns": ["Name", "Role", "Department", "Two-Layer Login", "Status"],
                "rows": [
                    [s.full_name, s.role, s.department, s.two_factor_mode, s.status]
                    for s in StaffUser.query.order_by(StaffUser.role.asc()).all()
                ],
            },
            {
                "title": "Emergency Registration Support",
                "columns": ["Patient", "Registered By", "Admission Type", "Ward"],
                "rows": [
                    [p.full_name, p.registered_by, p.admission_type, p.ward]
                    for p in Patient.query.order_by(Patient.admitted_on.desc()).all()
                ],
            },
        ]
        subtitle = "Operational access for generic hospital staff."

    return render_role_portal(
        "Staff Portal",
        subtitle,
        "Department",
        department,
        sections,
    )


@app.route("/pharmacy/portal")
def pharmacy_portal():
    return render_role_portal(
        "Pharmacy Portal",
        "Stock in, patient-used drugs, doctor prescription details, and admin-approved restock workflow.",
        "Restock queue",
        f"{PharmacyStock.query.filter(PharmacyStock.balance_units < 10).count()} low-stock medicines",
        [
            {
                "title": "Medical Stocks",
                "columns": ["Medicine", "Stock In", "Used", "Balance", "Approval", "Agency Order"],
                "rows": [
                    [m.medicine_name, str(m.stock_in), str(m.stock_out), str(m.balance_units), m.approval_status, m.order_status]
                    for m in PharmacyStock.query.order_by(PharmacyStock.medicine_name).all()
                ],
            },
            {
                "title": "Patient Drug Usage",
                "columns": ["Medicine", "Patient / Unit", "Doctor", "Balance"],
                "rows": [
                    [m.medicine_name, m.prescribed_to, m.prescribed_by, str(m.balance_units)]
                    for m in PharmacyStock.query.order_by(PharmacyStock.balance_units.asc()).all()
                ],
            },
        ],
    )


@app.route("/iot/portal")
def iot_portal():
    return render_role_portal(
        "IoT And Infant Security Portal",
        "Real-time patient anomaly monitoring and infant-band protection managed by the technical team.",
        "Active monitoring",
        f"{IotBandMonitor.query.count()} patient bands + {InfantSecurity.query.count()} infant bands",
        [
            {
                "title": "Patient IoT Bands",
                "columns": ["Patient", "Band Code", "Anomaly", "Heart Rate", "SpO2", "Temperature"],
                "rows": [
                    [r.patient_name, r.band_code, r.anomaly, str(r.heart_rate), f"{r.spo2}%", f"{r.temperature} F"]
                    for r in IotBandMonitor.query.order_by(IotBandMonitor.patient_name).all()
                ],
            },
            {
                "title": "Infant Band Security",
                "columns": ["Infant", "Mother", "Pair Code", "Authorized", "Alarm Status", "Alert Targets"],
                "rows": [
                    [i.infant_name, i.mother_name, i.pair_code, i.authorized_members, i.alarm_status, i.alert_targets]
                    for i in InfantSecurity.query.order_by(InfantSecurity.infant_name).all()
                ],
            },
        ],
    )


def setup_database() -> None:
    with app.app_context():
        db.create_all()
        if not using_mysql:
            seed_data()


setup_database()


if __name__ == "__main__":
    app.run(debug=True)
