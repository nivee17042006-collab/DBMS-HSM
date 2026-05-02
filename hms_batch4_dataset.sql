    alarm_status VARCHAR(150) NOT NULL,
    alert_targets VARCHAR(255) NOT NULL,
    technical_team VARCHAR(120) NOT NULL
);

-- Admin Account
INSERT INTO users (username, password, role) VALUES ('admin_root', 'admin@2026', 'Admin');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('admin_root', 'ADMIN123', 'Management');

-- Doctors
INSERT INTO users (username, password, role) VALUES ('dr_arjun', 'pass101', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_arjun', 'BIO_D_101', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_sneha', 'pass102', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_sneha', 'BIO_D_102', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_vikram', 'pass103', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_vikram', 'BIO_D_103', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_priya', 'pass104', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_priya', 'BIO_D_104', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_rohan', 'pass105', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_rohan', 'BIO_D_105', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_ananya', 'pass106', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_ananya', 'BIO_D_106', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_karthik', 'pass107', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_karthik', 'BIO_D_107', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_meera', 'pass108', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_meera', 'BIO_D_108', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_siddharth', 'pass109', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_siddharth', 'BIO_D_109', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_kavya', 'pass110', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_kavya', 'BIO_D_110', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_rahul', 'pass111', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_rahul', 'BIO_D_111', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_shalini', 'pass112', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_shalini', 'BIO_D_112', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_sanjay', 'pass113', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_sanjay', 'BIO_D_113', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_divya', 'pass114', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_divya', 'BIO_D_114', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_manoj', 'pass115', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_manoj', 'BIO_D_115', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_pooja', 'pass116', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_pooja', 'BIO_D_116', 'General');
INSERT INTO users (username, password, role) VALUES ('dr_naveen', 'pass117', 'Doctor');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('dr_naveen', 'BIO_D_117', 'General');

-- Nurses
INSERT INTO users (username, password, role) VALUES ('nurse_kavi', 'n201', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_kavi', 'BIO_N_201', 'Maternity (Infant)');
INSERT INTO users (username, password, role) VALUES ('nurse_deepa', 'n202', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_deepa', 'BIO_N_202', 'ICU');
INSERT INTO users (username, password, role) VALUES ('nurse_aruna', 'n203', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_aruna', 'BIO_N_203', 'Emergency Room');
INSERT INTO users (username, password, role) VALUES ('nurse_vidya', 'n204', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_vidya', 'BIO_N_204', 'Pediatrics');
INSERT INTO users (username, password, role) VALUES ('nurse_geetha', 'n205', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_geetha', 'BIO_N_205', 'General Ward A');
INSERT INTO users (username, password, role) VALUES ('nurse_mala', 'n206', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_mala', 'BIO_N_206', 'General Ward B');
INSERT INTO users (username, password, role) VALUES ('nurse_rekha', 'n207', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_rekha', 'BIO_N_207', 'Operation Theatre');
INSERT INTO users (username, password, role) VALUES ('nurse_sandhya', 'n208', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_sandhya', 'BIO_N_208', 'Cardiology');
INSERT INTO users (username, password, role) VALUES ('nurse_pavani', 'n209', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_pavani', 'BIO_N_209', 'Neurology');
INSERT INTO users (username, password, role) VALUES ('nurse_lakshmi', 'n210', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_lakshmi', 'BIO_N_210', 'Oncology');
INSERT INTO users (username, password, role) VALUES ('nurse_bhuvana', 'n211', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_bhuvana', 'BIO_N_211', 'Nephrology');
INSERT INTO users (username, password, role) VALUES ('nurse_divya', 'n212', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_divya', 'BIO_N_212', 'Orthopedics');
INSERT INTO users (username, password, role) VALUES ('nurse_meena', 'n213', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_meena', 'BIO_N_213', 'ENT Ward');
INSERT INTO users (username, password, role) VALUES ('nurse_rani', 'n214', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_rani', 'BIO_N_214', 'Psychiatry');
INSERT INTO users (username, password, role) VALUES ('nurse_shanthi', 'n215', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_shanthi', 'BIO_N_215', 'Outpatient Dept');
INSERT INTO users (username, password, role) VALUES ('nurse_kala', 'n216', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_kala', 'BIO_N_216', 'Post-Op Care');
INSERT INTO users (username, password, role) VALUES ('nurse_uma', 'n217', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_uma', 'BIO_N_217', 'Isolation Ward');
INSERT INTO users (username, password, role) VALUES ('nurse_nithya', 'n218', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_nithya', 'BIO_N_218', 'Dialysis Unit');
INSERT INTO users (username, password, role) VALUES ('nurse_hema', 'n219', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_hema', 'BIO_N_219', 'Lab & Diagnostics');
INSERT INTO users (username, password, role) VALUES ('nurse_preeti', 'n220', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_preeti', 'BIO_N_220', 'Radiology');
INSERT INTO users (username, password, role) VALUES ('nurse_sofia', 'n221', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_sofia', 'BIO_N_221', 'Burn Unit');
INSERT INTO users (username, password, role) VALUES ('nurse_amrutha', 'n222', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_amrutha', 'BIO_N_222', 'Physiotherapy');
INSERT INTO users (username, password, role) VALUES ('nurse_ishani', 'n223', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_ishani', 'BIO_N_223', 'Trauma Center');
INSERT INTO users (username, password, role) VALUES ('nurse_yamini', 'n224', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_yamini', 'BIO_N_224', 'Blood Bank');
INSERT INTO users (username, password, role) VALUES ('nurse_tara', 'n225', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_tara', 'BIO_N_225', 'Pharmacy Support');
INSERT INTO users (username, password, role) VALUES ('nurse_jaya', 'n226', 'Nurse');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('nurse_jaya', 'BIO_N_226', 'Reception/Triage');

-- Staff
INSERT INTO users (username, password, role) VALUES ('staff_rahul', 's301', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_rahul', 'BIO_S_301', 'Pharmacy Manager');
INSERT INTO users (username, password, role) VALUES ('staff_meena', 's302', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_meena', 'BIO_S_302', 'Receptionist');
INSERT INTO users (username, password, role) VALUES ('staff_vikram', 's303', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_vikram', 'BIO_S_303', 'Lab Technician');
INSERT INTO users (username, password, role) VALUES ('staff_sonia', 's304', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_sonia', 'BIO_S_304', 'Billing Clerk');
INSERT INTO users (username, password, role) VALUES ('staff_arjun', 's305', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_arjun', 'BIO_S_305', 'Security Head');
INSERT INTO users (username, password, role) VALUES ('staff_priya', 's306', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_priya', 'BIO_S_306', 'HR Coordinator');
INSERT INTO users (username, password, role) VALUES ('staff_karthik', 's307', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_karthik', 'BIO_S_307', 'IT Support / AI');
INSERT INTO users (username, password, role) VALUES ('staff_divya', 's308', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_divya', 'BIO_S_308', 'Medical Records');
INSERT INTO users (username, password, role) VALUES ('staff_sanjay', 's309', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_sanjay', 'BIO_S_309', 'Maintenance');
INSERT INTO users (username, password, role) VALUES ('staff_ananya', 's310', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('staff_ananya', 'BIO_S_310', 'Cafeteria Admin');
INSERT INTO users (username, password, role) VALUES ('clean_mani', 'c301', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('clean_mani', 'BIO_C_301', 'Cleaning - Maternity');
INSERT INTO users (username, password, role) VALUES ('clean_senthil', 'c304', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('clean_senthil', 'BIO_C_304', 'Cleaning - ICU');
INSERT INTO users (username, password, role) VALUES ('clean_velu', 'c307', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('clean_velu', 'BIO_C_307', 'Cleaning - General');
INSERT INTO users (username, password, role) VALUES ('clean_arun', 'c308', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('clean_arun', 'BIO_C_308', 'Cleaning - Cardio');
INSERT INTO users (username, password, role) VALUES ('clean_mala', 'c309', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('clean_mala', 'BIO_C_309', 'Cleaning - Pedia');
INSERT INTO users (username, password, role) VALUES ('clean_kumar', 'c310', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('clean_kumar', 'BIO_C_310', 'Cleaning - Ortho');
INSERT INTO users (username, password, role) VALUES ('clean_latha', 'c311', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('clean_latha', 'BIO_C_311', 'Cleaning - ENT');
INSERT INTO users (username, password, role) VALUES ('clean_vicky', 'c312', 'Staff');
INSERT INTO access_layers (username, biothumb_id, department) VALUES ('clean_vicky', 'BIO_C_312', 'Cleaning - Emergency');

-- Doctors table dataset used by the app
INSERT INTO doctors (full_name, department, availability, assigned_ward) VALUES
('Dr. Arjun', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Sneha', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Vikram', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Priya', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Rohan', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Ananya', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Karthik', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Meera', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Siddharth', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Kavya', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Rahul', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Shalini', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Sanjay', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Divya', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Manoj', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Pooja', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General'),
('Dr. Naveen', 'General', 'Mon-Sat, 9 AM - 5 PM', 'General');

-- Core demo data used in the website
INSERT INTO patients (full_name, age, gender, phone, patient_condition, ward, admission_type, registered_by, emergency_case, admitted_on) VALUES
('Kaviya Raj', 29, 'Female', '9876543210', 'Post-surgery recovery', 'Ward A', 'Inpatient', 'Admin', FALSE, '2026-04-14'),
('Arjun Kumar', 41, 'Male', '9789012345', 'Cardiac observation', 'ICU 2', 'Emergency', 'Receptionist', TRUE, '2026-04-15');

INSERT INTO ward_assignments (patient_name, doctor_name, nurse_name, ward_name, room_number, schedule_note) VALUES
('Arjun Kumar', 'Dr. Arjun', 'Nurse Deepa', 'ICU 2', 'ICU-08', 'Vitals every 2 hours'),
('Kaviya Raj', 'Dr. Sneha', 'Nurse Kavi', 'Ward A', 'A-12', 'Morning and evening rounds');

INSERT INTO prescriptions (patient_name, doctor_name, nurse_name, medicines, dosage, prescribed_on) VALUES
('Arjun Kumar', 'Dr. Arjun', 'Nurse Deepa', 'Aspirin, Atorvastatin', '1-0-1 for 5 days', '2026-04-15'),
('Kaviya Raj', 'Dr. Sneha', 'Nurse Kavi', 'Paracetamol, Cefixime', '1-1-1 after food', '2026-04-16');

INSERT INTO pharmacy_stock (medicine_name, stock_in, stock_out, balance_units, prescribed_to, prescribed_by, approval_status, order_status) VALUES
('Aspirin', 100, 24, 76, 'Arjun Kumar', 'Dr. Arjun', 'Approved by Admin', 'In stock'),
('Infant Vitamin Drops', 20, 18, 2, 'NICU', 'Dr. Sneha', 'Awaiting Admin Approval', 'Restock requested');

INSERT INTO iot_band_monitor (patient_name, band_code, anomaly, heart_rate, spo2, temperature, monitored_by, last_sync) VALUES
('Arjun Kumar', 'IOT-ARJ-2201', 'Irregular heart rate detected', 122, 93, 99.4, 'Staff Karthik', '16 Apr 2026, 08:45 AM'),
('Kaviya Raj', 'IOT-KAV-1140', 'No anomaly', 82, 98, 98.4, 'Staff Karthik', '16 Apr 2026, 08:50 AM');

INSERT INTO infant_security (infant_name, mother_name, pair_code, authorized_members, alarm_status, alert_targets, technical_team) VALUES
('Baby Diya', 'Meena S', 'MOM-INF-9088', 'Mother, Dr. Sneha, Nurse Kavi', 'Protected', 'Reception, Doctor, Nurse', 'Staff Karthik'),
('Baby Keshav', 'Anu K', 'MOM-INF-9011', 'Mother, NICU doctor, Assigned nurse', 'Band tamper alert test enabled', 'Reception, NICU Desk, Nurse Station', 'Staff Karthik');

DELIMITER $$

CREATE PROCEDURE AddPatient(
    IN p_full_name VARCHAR(120),
    IN p_age INT,
    IN p_gender VARCHAR(20),
    IN p_phone VARCHAR(20),
    IN p_condition VARCHAR(150),
    IN p_ward VARCHAR(100),
    IN p_admission_type VARCHAR(50),
    IN p_registered_by VARCHAR(50),
    IN p_emergency_case BOOLEAN,
    IN p_admitted_on DATE
)
BEGIN
    INSERT INTO patients (
        full_name, age, gender, phone, patient_condition, ward,
        admission_type, registered_by, emergency_case, admitted_on
    )
    VALUES (
        p_full_name, p_age, p_gender, p_phone, p_condition, p_ward,
        p_admission_type, p_registered_by, p_emergency_case, p_admitted_on
    );
END $$

CREATE PROCEDURE GetPatientDetails()
BEGIN
    SELECT * FROM patients;
END $$

CREATE PROCEDURE ValidateStaffLogin(
    IN p_username VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_biothumb_id VARCHAR(100)
)
BEGIN
    SELECT u.username, u.role, a.department
    FROM users u
    JOIN access_layers a ON u.username = a.username
    WHERE u.username = p_username
      AND u.password = p_password
      AND a.biothumb_id = p_biothumb_id;
END $$

CREATE PROCEDURE GetDoctorPatients()
BEGIN
    SELECT full_name, patient_condition, ward, registered_by
    FROM patients;
END $$

CREATE PROCEDURE GetNursePatientDetails()
BEGIN
    SELECT full_name, age, patient_condition, ward, emergency_case
    FROM patients;
END $$

CREATE PROCEDURE UpdatePharmacyStock(
    IN p_medicine_name VARCHAR(120),
    IN p_stock_in INT,
    IN p_stock_out INT,
    IN p_balance_units INT,
    IN p_prescribed_to VARCHAR(120),
    IN p_prescribed_by VARCHAR(120),
    IN p_approval_status VARCHAR(80),
    IN p_order_status VARCHAR(80)
)
BEGIN
    INSERT INTO pharmacy_stock (
        medicine_name, stock_in, stock_out, balance_units,
        prescribed_to, prescribed_by, approval_status, order_status
    )
    VALUES (
        p_medicine_name, p_stock_in, p_stock_out, p_balance_units,
        p_prescribed_to, p_prescribed_by, p_approval_status, p_order_status
    );
END $$

CREATE PROCEDURE GetIotAlerts()
BEGIN
    SELECT patient_name, band_code, anomaly, heart_rate, spo2, temperature
    FROM iot_band_monitor
    WHERE anomaly <> 'No anomaly';
END $$

CREATE PROCEDURE GetAdminSummary()
BEGIN
    SELECT
        (SELECT COUNT(*) FROM patients) AS total_patients,
        (SELECT COUNT(*) FROM doctors) AS total_doctors,
        (SELECT COUNT(*) FROM users) AS total_users,
        (SELECT COUNT(*) FROM iot_band_monitor WHERE anomaly <> 'No anomaly') AS critical_alerts;
END $$

DELIMITER ;
