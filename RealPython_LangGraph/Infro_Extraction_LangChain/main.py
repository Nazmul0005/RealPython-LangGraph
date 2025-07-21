from chains.notice_extraction import NOTICE_PARSER_CHAIN
from example_emails import EMAILS
NOTICE_PARSER_CHAIN.invoke({"message": EMAILS[0]})
NoticeEmailExtract(
    entity_name='Occupational Safety and Health Administration (OSHA)',
    entity_phone='(555) 123-4567',
    entity_email='compliance.osha@osha.gov',
    project_id=111232345,
    site_location='123 Main Street, Dallas, TX',
    violation_type='Lack of fall protection, Unsafe scaffolding setup,
        Inadequate personal protective equipment (PPE)',
    required_changes='Install guardrails and fall arrest systems on all
        scaffolding over 10 feet. Conduct an inspection of all scaffolding
        structures and reinforce unstable sections. Ensure all workers
        on-site are provided with necessary PPE and conduct safety training
        on proper usage.',
    max_potential_fine=25000.0,
    date_of_notice=datetime.date(2024, 10, 15),
    compliance_deadline=datetime.date(2024, 11, 10)
)