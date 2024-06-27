import argparse

# Complete list of centres with services
centres = [
    {
        "name": "Brantford Regional Indigenous Support Centre (BRISC)",
        "address": "318 1/2 Colborne Street E., Brantford, ON N3S 3N1",
        "phone": "519-304-7400",
        "services": [
            "Healing and Wellness Coordinator Program",
            "Indigenous Court Work Program",
            "Education and Employment",
            "Homelessness and Housing",
            "Apatisiwin - Employment & Training Program",
            "Urban programming for Indigenous people"
        ]
    },
    {
        "name": "Hamilton Regional Indian Centre",
        "address": "34 Ottawa St. North, Hamilton, ON L8H 3Y7",
        "phone": "905-545-4077",
        "email": "support@hric.ca",
        "website": "http://www.hric.ca",
        "services": [
            "Strengthening Hamilton Aboriginal Education (SHAE)",
            "Apatisiwin - Employment & Training Program",
            "Aboriginal Alcohol/Drug Program",
            "Aboriginal Criminal/Family Court Work Program",
            "Aboriginal Family Support Program",
            "Aboriginal Healthy Babies/Healthy Children Program",
            "Aboriginal Prenatal/Nutrition Program",
            "Fetal Alcohol Spectrum Disorder (FASD) and Nutrition Program",
            "Indigenous Youth Wellness Program"
        ]
    },
    {
        "name": "Fort Erie Native Friendship Centre",
        "address": "796 Buffalo Road, Fort Erie, ON L2A 5H2",
        "phone": "905-871-8931",
        "email": "reception@fenfc.org",
        "website": "http://www.fenfc.org",
        "services": [
            "Aboriginal Healthy Babies Healthy Children",
            "Canadian Prenatal Nutrition Program",
            "Aboriginal Family Support",
            "EarlyON & Tshikeksa (When I was a Child) Resource Room",
            "Under the Rainbow Childcare Centre",
            "Courage to Soar (Education)",
            "Youth Navigator",
            "Apatisiwin Employment Unit",
            "Grand River Employment & Training",
            "Indigenous Court Worker",
            "Urban Aboriginal Healthy Living Program",
            "Cultural Resource Coordinator",
            "Aboriginal Alcohol and Drug Worker",
            "Mental Health Wellness",
            "Academic Upgrading Program (A.C.E.)",
            "Health Outreach",
            "Life Long Care",
            "Indigenous Homeward Bound"
        ]
    },
    {
        "name": "Kapuskasing Indian Friendship Centre",
        "address": "41 Murdock Street, Kapuskasing, ON P5N 1H9",
        "phone": "705-337-1935",
        "website": "https://kifc.ca",
        "services": [
            "Apatisiwin- Employment and Training Program",
            "Cultural Resource Coordinator",
            "Healing and Wellness Coordinator Program",
            "Indigenous Healthy Babies Healthy Children Program",
            "Healthy Living Program",
            "Student Nutrition Program",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "United Native Friendship Centre (Fort Frances)",
        "address": "516 Portage Ave, Fort Frances, ON P9A 3N1",
        "phone": "807-274-8541",
        "website": "https://unfc.org",
        "services": [
            "Student Nutrition Program",
            "Alternative Secondary School Program",
            "Employment and Training Program",
            "Children’s Mental Health Program",
            "Indigenous Mental Health and Wellness Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healing and Wellness Coordinator Program",
            "Healthy Kids Program/Healthy Living Program",
            "Life Long Care Program",
            "Reaching Home Program",
            "Youth Culture Camps"
        ]
    },
    {
        "name": "Toronto Council Fire Native Cultural Centre",
        "address": "439 Dundas St. East, Toronto, ON M5A 2B1",
        "phone": "416-360-4350",
        "website": "http://www.councilfire.ca",
        "services": [
            "Student Nutrition Program",
            "Cultural Resource Coordinator",
            "Healing and Wellness Coordinator Program",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Programming for Indigenous Peoples – Programs and Services",
            "Youth Life Promotion",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Timmins Native Friendship Centre",
        "address": "179 Kirby Ave., Timmins, ON P4N 1K1",
        "phone": "705-268-6262",
        "email": "reception@tnfc.ca",
        "website": "http://www.tnfc.ca",
        "services": [
            "Aboriginal Alternative Secondary School Program",
            "Aboriginal Court Worker Program",
            "Aboriginal Alcohol and Drug Worker Program",
            "Aboriginal Family Support and Wellness Program",
            "Aboriginal Healing and Wellness Strategy Program",
            "Aboriginal Healthy Babies Healthy Children Program",
            "Aboriginal Prenatal Nutrition Program",
            "Academic and Career Entrance Program",
            "Community Career Developer"
        ]
    },
    {
        "name": "Thunderbird Friendship Centre (Geraldton)",
        "address": "301 Beamish Ave. W., Geraldton, ON P0T 1M0",
        "phone": "807-854-1060",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Cultural Resource Coordinator",
            "Indigenous Mental Health and Wellness Program",
            "Indigenous Court Work Program",
            "Indigenous Community Justice Program",
            "Healing and Wellness Coordinator Program",
            "Healthy Living Program",
            "Health Outreach Worker Program",
            "Life Long Care Program",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Thunder Bay Indigenous Friendship Centre",
        "address": "401 N. Cumberland St., Thunder Bay, ON P7A 4P7",
        "phone": "807-345-5840",
        "website": "https://tbifc.ca",
        "services": [
            "Aboriginal Alcohol/Drug Worker Program",
            "Indigenous Community Council Program",
            "Aboriginal Family Support Program",
            "Indigenous Healing and Wellness",
            "Anishnawbe Skills Development Program",
            "Employment Program",
            "Children’s Wellness Program",
            "Indigenous Court Work Program",
            "Community Support Program",
            "Reaching Home: Canada’s Homelessness Strategy",
            "Indigenous Peoples’ Court Case Worker",
            "The Gladue Services Program (Writer and Aftercare)",
            "Youth Justice Committee",
            "Youth Life Promotions"
        ]
    },
    {
        "name": "Sarnia-Lambton Native Friendship Centre",
        "address": "223 Lochiel St., Sarnia, ON N7T 4C9",
        "phone": "519-344-6164",
        "email": "info@slnfc.org",
        "website": "http://slnfc.org",
        "services": [
            "Cultural Resource Coordinator",
            "Student Nutrition Program",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Programming for Indigenous Peoples – Programs and Services"
        ]
    },
    {
        "name": "Red Lake Indian Friendship Centre",
        "address": "1 Legion Road, Red Lake, ON P0V 2M0",
        "phone": "807-727-2847",
        "email": "Friends@rlifc.ca",
        "website": "http://rlifc.ca",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Alternative Secondary School Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Fetal Alcohol Spectrum Disorder/Child Nutrition Program",
            "Healing and Wellness Coordinator Program",
            "Healthy Kids Program",
            "Healthy Living Program",
            "Health Outreach Worker Program",
            "Urban Programming for Indigenous Peoples"
        ]
    },
    {
        "name": "The Indigenous Network",
        "address": "208 Britannia Rd East, Unit 1, Mississauga, ON L4Z 1S6",
        "phone": "905-712-4726",
        "website": "http://theindigenousnetwork.com",
        "email": "info@theindigenousnetwork.com",
        "services": [
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Parry Sound Friendship Centre",
        "address": "25 Church St., Parry Sound, ON P2A 1Y2",
        "phone": "705-746-5970",
        "website": "https://psfc.ca/",
        "services": [
            "Student Nutrition Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healing and Wellness Coordinator Program",
            "Healthy Living Program",
            "Health Outreach Worker Program",
            "Life Long Care Program",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Odawa Native Friendship Centre",
        "address": "815 St. Laurent Blvd., Ottawa, ON K1K 3A7",
        "phone": "613-722-3811",
        "email": "reception@odawa.on.ca",
        "website": "https://odawafc.com/",
        "services": [
            "Student Nutrition Program",
            "Alternative Secondary School Program",
            "Indigenous Court Work Program",
            "Indigenous Community Justice Program",
            "Cultural Resource Coordinator",
            "Healing and Wellness Coordinator Program",
            "Indigenous Healthy Babies Healthy Children Program",
            "Life Long Care Program",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "North Bay Indigenous Friendship Centre",
        "address": "980 Cassells St, North Bay, ON P1B 4A6",
        "phone": "705-472-2811",
        "email": "reception@nbifc.org",
        "website": "https://nbifc.org",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Children Who Witness Violence Program",
            "Indigenous Court Work Program",
            "Indigenous Community Justice Program",
            "Cultural Resource Coordinator",
            "Healing and Wellness Coordinator Program",
            "Indigenous Healthy Babies Healthy Children Program",
            "Life Long Care Program",
            "Indigenous Friendship Centre Program",
            "Youth Life Promotion"
        ]
    },
    {
        "name": "Nogojiwanong Friendship Centre (Peterborough)",
        "address": "580 Cameron St. Peterborough, ON K9J 3Z5",
        "phone": "705-775-0387",
        "email": "admin@nogofc.ca",
        "website": "https://www.nogofc.ca",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Indigenous Mental Health and Wellness Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Kids Program",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Indigenous Homeward Bound",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Nishnawbe-Gamik Friendship Centre (Sioux Lookout)",
        "address": "52 King Street, Sioux Lookout, ON P8T 1B8",
        "phone": "807-737-1903",
        "website": "http://www.ngfc.net",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Indigenous Mental Health and Wellness Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Kids Program",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Indigenous Homeward Bound",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Niagara Regional Native Centre (Niagara-On-The-Lake)",
        "address": "382 Airport Rd, Niagara-On-The-Lake, ON L0S 1J0",
        "phone": "905-688-6484",
        "website": "https://nrnc.ca",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Children’s Mental Health Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Kids Program",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Indigenous Homeward Bound",
            "Urban Programming for Indigenous Peoples – Programs and Services",
            "Indigenous Friendship Centre Program",
            "Health Outreach Worker Program",
            "Reaching Home Program"
        ]
    },
    {
        "name": "Ne-Chee Friendship Centre (Kenora)",
        "address": "326 2nd Street S., Kenora, ON P9N 1G5",
        "phone": "807-468-5440",
        "email": "reception@nechee.org",
        "website": "https://www.nechee.org",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Alternative Secondary School Program",
            "Children Who Witness Violence Program",
            "Indigenous Court Work Program",
            "Indigenous Community Justice Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program",
            "Youth Life Promotion"
        ]
    },
    {
        "name": "N'Swakamok Native Friendship Centre (Sudbury)",
        "address": "110 Elm St West, Sudbury, ON P3C 1T5",
        "phone": "705-674-2128",
        "website": "http://www.nfcsudbury.org",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Alternative Secondary School Program",
            "Children’s Mental Health Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Fetal Alcohol Spectrum Disorder/Child Nutrition Program",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "N'Amerind Friendship Centre (London)",
        "address": "260 Colborne St, London, ON N6B 2S6",
        "phone": "519-672-0131",
        "website": "http://namerind.on.ca",
        "services": [
            "Employment and Training Program",
            "Alternative Secondary School Program",
            "Indigenous Mental Health and Wellness Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Indigenous Homeward Bound",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program",
            "Student Nutrition Program"
        ]
    },
    {
        "name": "M'Wikwedong Native Cultural Resource Centre (Owen Sound)",
        "address": "1045 Third Ave West, Owen Sound, ON N4K 5W6",
        "phone": "519-371-1147",
        "email": "admin@mwikwedong.com",
        "website": "https://mwikwedong.com",
        "services": [
            "Employment and Training Program",
            "Children Who Witness Violence Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program",
            "Youth Culture Camps"
        ]
    },
    {
        "name": "Ininew Friendship Centre (Cochrane)",
        "address": "190 Third Ave, Cochrane ON P0L 1C0",
        "phone": "705-272-4497",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Children’s Mental Health Program",
            "Indigenous Mental Health and Wellness Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Health Outreach Worker Program",
            "Reaching Home Program",
            "Urban Programming for Indigenous Peoples – Programs and Services",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "The Indian Friendship Centre in Sault Ste. Marie",
        "address": "122 East St, Sault Ste. Marie, ON P6A 3C6",
        "phone": "705-256-5634",
        "email": "recept@gbnfc.com",
        "website": "http://www.ssmifc.com",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Indigenous Mental Health and Wellness Program",
            "Alternative Secondary School Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Reaching Home Program",
            "Urban Indigenous Homeward Bound",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Georgian Bay Native Friendship Centre (Midland)",
        "address": "175 Yonge St, Midland, ON L4R 2A7",
        "phone": "705-526-5589",
        "website": "https://www.gbnfc.com",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Children Who Witness Violence Program",
            "Indigenous Mental Health and Wellness Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Reaching Home Program",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program",
            "Youth Life Promotion"
        ]
    },
    {
        "name": "Dryden Native Friendship Centre",
        "address": "74 Queen St, Dryden ON, P8N 1A4",
        "phone": "1-888-838-3632",
        "website": "https://www.dnfconline.org",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Children Who Witness Violence Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Indigenous Homeward Bound",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Cam-Am Indian Friendship Centre of Windsor",
        "address": "2929 Howard Ave., Windsor, ON N8X 4W4",
        "phone": "519-253-3243",
        "email": "admin@caifc.ca",
        "website": "https://caifc.ca",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Indigenous Mental Health and Wellness Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Reaching Home Program",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program",
            "Youth Life Promotion",
            "Alternative Secondary School Program",
            "Health Outreach Worker Program"
        ]
    },
    {
        "name": "Barrie Native Friendship Centre",
        "address": "175 Bayfield St, Barrie, ON L4M 3B4",
        "phone": "705-721-7689",
        "website": "https://www.barrienfc.ca",
        "services": [
            "Student Nutrition Program",
            "Employment and Training Program",
            "Indigenous Healthy Babies Healthy Children Program",
            "Indigenous Court Work Program",
            "Cultural Resource Coordinator",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program"
        ]
    },
    {
        "name": "Atikokan Native Friendship Centre",
        "address": "307-309 Main St. W, Atikokan, ON P0T 1C0",
        "phone": "807-597-1213",
        "services": [
            "Student Nutrition Program",
            "Indigenous Court Work Program",
            "Healthy Living Program",
            "Life Long Care Program",
            "Urban Indigenous Homeward Bound",
            "Urban Programming for Indigenous Peoples",
            "Indigenous Friendship Centre Program",
            "Healing and Wellness Coordinator Program"
        ]
    }
]

def get_all_centres():
    for centre in centres:
        print(f"Name: {centre['name']}")
        print(f"Address: {centre['address']}")
        print(f"Phone: {centre['phone']}")
        if 'email' in centre:
            print(f"Email: {centre['email']}")
        if 'website' in centre:
            print(f"Website: {centre['website']}")
        print("Services:")
        for service in centre.get('services', []):
            print(f"  - {service}")
        print("\n")

def get_centre(name):
    for centre in centres:
        if name.lower() in centre['name'].lower():
            print(f"Name: {centre['name']}")
            print(f"Address: {centre['address']}")
            print(f"Phone: {centre['phone']}")
            if 'email' in centre:
                print(f"Email: {centre['email']}")
            if 'website' in centre:
                print(f"Website: {centre['website']}")
            print("Services:")
            for service in centre.get('services', []):
                print(f"  - {service}")
            print("\n")
            return
    print("Centre not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Indigenous Friendship Centres Info')
    parser.add_argument('--all', action='store_true', help='Get all centres')
    parser.add_argument('--name', type=str, help='Get centre by name')

    args = parser.parse_args()

    if args.all:
        get_all_centres()
    elif args.name:
        get_centre(args.name)
    else:
        print("Please provide a valid argument. Use --help for more info.")
            
