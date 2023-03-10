-- 코드를 입력하세요
SELECT APNT_NO,PT_NAME, PT_NO, DOCTOR.MCDP_CD,DR_NAME,APNT_YMD
FROM PATIENT
INNER JOIN APPOINTMENT USING (PT_NO)
INNER JOIN DOCTOR ON APPOINTMENT.MDDR_ID = DOCTOR.DR_ID
WHERE DOCTOR.MCDP_CD = 'CS' AND MONTH(APNT_YMD) = '4' AND DAY(APNT_YMD) = '13' AND APNT_CNCL_YN = 'N'
ORDER BY APNT_YMD;

# APPOINTMENT테이블의 APNT_CNCL_YMD가 예약취소날짜
# APNT_YMD 진료 예약일시  가 4월13일이고 취소 여부가 N인 경우


# MDDR_ID