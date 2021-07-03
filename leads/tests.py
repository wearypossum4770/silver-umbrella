import pytest
from django.test import Client, TestCase

from leads.models import Lead


# response = client.get('/foo/')
pytestmark = pytest.mark.django_db
class TestLead(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client(enforce_csrf_checks=True)
        Lead.objects.create(
            company="Lynx Dx",
            location="333 Jackson Plaza Suite 600 Ann Arbor, MI, 48103",
            base_salary="70000.00",
            min_salary="60000.00",
            max_salary="120000.00",
            role_name="Junior Software Engineer",
            remote_position=True,
            start_date=None,
            end_date=None,
            employment_type="FT",
            employer_overview="Join a dynamic, growing company tackling the world’s largest public health crisis. We are scientists, engineers, informaticists, pioneers, parents, students, researchers — and we are passionate about solving some of the world’s toughest challenges in healthcare.  LynxDx is a biotechnology company founded to commercialize a groundbreaking prostate cancer diagnostic test, known as MyProstateScore (MPS). This emerged from a genomic discovery made at the University of Michigan, from which the company is spun out of.  As the pandemic emerged in 2020, the company shifted its focus to COVID-19 PCR testing. Since the first test performed in May 2020, the lab grew to one of Michigan’s largest providers of COVID testing. Our COVID testing program is used by the University of Michigan, local hospitals, community drive-thrus, athletic programs, K-12 schools, and other partners across the State.  As part of our software development team, you will be working to develop and maintain our in-house custom-built laboratory information management system (LIMS), which powers all lab operations, direct-to-patient result reporting, and more.",
            experience_requirements="javascript, python, backend, sql, postgresql, git, command line,",
            experience_preferred="google cloud, react, testing, previous startup,azure",
            application_submission="employment/job_applications/2021/05/04/app.pdf",
            application_status="APP",
            notes="",
        ).save()
        cls.example_lead = Lead.objects.all()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_lead_creation(self):
        lead = self.example_lead
        assert len(lead) > 0
    def test_lead_list_endpoint_redirect(self):
        response  = self.client.get('/leads')
        assert response.status_code ==301
    def test_lead_list_endpoint(self):
        response  = self.client.get('/leads/')
        assert response.status_code ==200
        # def test_

        # measurementTechnique
        # https://schema.org/usedToDiagnose
        # https://schema.org/relatedCondition
        # https://schema.org/typicalTest
        # https://schema.org/guideline
        # https://schema.org/identifier


header = {
        "ContentDate": "lei:LEIDateTimeProfile",
        "Originator": "lei:LEIType",
        "FileContent": "lei:FileContentEnum",
        "DeltaStart": "lei:LEIDateTimeProfile",
        "RecordCount": "xs:nonNegativeInteger",
        "Extension": "lei:ExtensionType ",
      
}
registration = {
    
        "InitialRegistrationDate": "lei:LEIDateTimeProfile",
        "LastUpdateDate": "lei:LEIDateTimeProfile",
        "RegistrationStatus": "lei:RegistrationStatusEnum",
        "NextRenewalDate": "lei:LEIDateTimeProfile",
        "ManagingLOU": "lei:LEIType",
        "ValidationSources": "ValidationSourcesTypeEnum",
        "ValidationAuthority": "lei:ValidationAuthorityType",
        "OtherValidationAuthorities": "lei:OtherValidationAuthoritiesType",
}
entity = {
"LEI" :"lei:LEIType", 
"LegalName": "lei:NameType",
"OtherEntityNames": "lei:OtherEntityNamesType",
"TransliteratedOtherEntityNames": "lei:TransliteratedOtherEntityNamesType",
"LegalAddress": "lei:AddressType",
"HeadquartersAddress": "lei:AddressType",
"OtherAddresses": "lei:OtherAddressesType",
"TransliteratedOtherAddresses": "lei:TransliteratedOtherAddressesType",
"RegistrationAuthority": "lei:RegistrationAuthorityType",
"LegalJurisdiction": "lei:JurisdictionCodeType",
"EntityCategory": "lei:EntityCategoryTypeEnu",
"LegalForm": "lei:LegalFormType",
"AssociatedEntity": "lei:AssociatedEntityType",
"EntityStatus": "lei:EntityStatusEnum",
"EntityExpirationDate": "lei:LEIDateTimeProfile",
"EntityExpirationReason": "lei:EntityExpirationReasonEnum",
"SuccessorEntity": "lei:SuccessorEntityType",
}


______id = (
    # '8ade75b4-9925-4350-a7e2-f78fa0e6222a',
'7fb73e5e-acb1-4001-870b-bb3dc4cda6d5',
'65b39ca5-47ea-45d5-b8d9-b77d4449be8e',
'067642cc-f339-43e1-8ac4-adae1e64df03',
'14cf9992-4283-4749-a995-d9ca8364ef7c',
'f7ef9a1e-2843-4e35-a9e6-504545199d21',
'477f86dc-f164-43d4-955b-e9da13797578',
'9ba8f0ab-cdb5-45f1-aec1-984425446310',
'33cdb472-8fa2-4701-92c8-e6e589883915',
'26cd4f27-a3ea-4591-a6b8-de494c35ed13',
'e8eecec5-9237-4aeb-b30c-a5c35d07a065',
'8c5d0509-c2a9-40d3-91fa-45a69cdbd298',
'c3093911-0ed8-446d-b833-f9f9b6c8e916',
'6b564017-338e-457b-a031-a45463398695',
'84dd9f58-0655-411e-8fdd-43ea925439a5',
'44e1ffd8-7fa7-4160-9ac1-31b3f7afb593',
'ae0e5563-5516-4bf6-b178-571ad534dc9b'
'91d6365b-dfe2-45ce-a652-5cbe39fa5b11',
# 'ckobrtszt000064veagsjvip6',
'ckobrtu61000164vekrafro67',
'ckobrtus1000264ve9ano3zh1',
'ckobrtv9t000364veq73qb743',
'ckobrtvnk000464veazyac3wi',
'ckobrtvyp000564veg9le2eh7',
'ckobrtwjd000664verywgpnyq',
'ckobrtyqx000764ve8v3srnyp',
'ckobrtz1t000864ve3061rx7s',
'ckobrtz9l000964vedoxe8c51',
'ckobrtzgh000a64veit25r7zm',
'ckobrtznc000b64ve1msov2hr',
'ckobrtzup000c64vehy00l39t',
'ckobru035000d64vex5yl9c7e',
'ckobru0c9000e64velh0qyzem',
'ckobru0pk000f64vecc47sjtp',
'ckobru0ve000g64ves50y63gh',
'ckobru101000h64vewb0hgo6v',
'ckobru14x000i64vewgwl4vip',
'ckobru19l000j64velo943ekv',
'ckobru1e9000k64veks5c22iy',
'ckobru1iw000l64vecvupxhap',
'ckobru1nd000m64ve4cl60set',
'ckobru1rd000n64vezkkszohd',
'ckobru1uh000o64ve38fu3r3y',
'ckobru1yh000p64vegz8160c0',
)