import csv
import collections
import itertools
import sys
from  datetime import datetime
from collections import defaultdict

csv.field_size_limit(sys.maxsize)

"""
Name :  Aniket Gaikwad
description : This file implements Feature generation functions.
"""

class featureGen:
    """
    Desc : Generate features from 'Business' & 'Review' files.
    """
    def __init__(self):
        #self.fileName=None
        self.BusinessToCategory=None
        self.listOfCategory=None
        self.featureVector=None

    def getBusinesSToCato(self,fileName):
        """
        Desc : Get descritized categories from business file and attributes & combine them to generate feature set.
        Args:
            fileName: Input file

        Returns: None

        """
        ## Open file & get all categories
        print('\n Business Vector build starts....')
        fr=csv.reader(open(fileName,'r'))
        l=[]
        firstRow=True
        tempDict={}
        for row in fr:
            businessVect=[]
            print('\n Len of Business File entry : {0}').format(len(row))
            if(firstRow):
                #print('\n row : {0}').format(row)
                categoryHead=row[105:]
                """
                categoryHead=['', 'Men_Clothing', 'Diners', 'SkatingRinks', 'Magicians', 'Arcades', 'Irrigation', \
                              'DamageRestoration', 'HairRemoval', 'Japanese', 'ChildCare&DayCare', 'Fitness&Instruction',\
                              'MotorcycleRepair', 'Cupcakes', 'Propane', 'OccupationalTherapy', 'HangGliding',\
                              'DepartmentsofMotorVehicles', 'Electricians', 'Irish', 'Distilleries', 'MiddleSchools&HighSchools',\
                              'LifeCoach', 'FacePainting', 'LatinAmerican', 'FireplaceServices', 'Accessories', 'Advertising',\
                              'Eyewear&Opticians', 'PetStores', 'KidsActivities', 'BotanicalGardens', 'Musicians', 'Doctors', \
                              'FlightInstruction', 'ShavedIce', 'BabyGear&Furniture', 'PediatricDentists', 'Patisserie/CakeShop',\
                              'HotPot', 'Endodontists', 'BeverageStore', 'Tanning', 'Soup', 'DaySpas', 'Herbs&Spices',\
                              'AutoDetailing', 'Sandwiches', 'SocialClubs', 'BailBondsmen', 'Adult', 'Orthotics', 'Allergists',\
                              'AirportLounges', 'Wheel&RimRepair', 'Reiki', 'GoKarts', 'Airlines', 'Utilities', 'CocktailBars',\
                              'UsedBookstore', 'Midwives', 'Podiatrists', 'Pop-upShops', 'FoodTrucks', 'CheeseShops', \
                              'AdultEducation', 'FabricStores', 'Paintball', 'FurnitureReupholstery', 'FoodStands', 'Grocery',\
                              'HomeHealthCare', 'Vocational&TechnicalSchool', 'Pilates', 'Czech', 'Basque', 'PlusSizeFashion',\
                              'VacationRentalAgents', 'SharedOfficeSpaces', 'MetalFabricators', 'BoatCharters', 'DataRecovery',\
                              'InternalMedicine', 'WaterDelivery', 'Saunas', 'LaserEyeSurgery/Lasik', 'TanningBeds',\
                              'AutoGlassServices', 'WebDesign', 'CarShareServices', 'Fishing', 'MedicalCenters', 'EarNose&Throat',\
                              'InsulationInstallation', 'OutletStores', 'AutoParts&Supplies', 'Marketing', 'Ramen', \
                              'RecreationCenters', 'KnittingSupplies', 'LactationServices', 'Taiwanese', 'Canadian(New)',\
                              'CandyStores', 'Diving', 'CosmetologySchools', 'PrintingServices', 'BikeRepair/Maintenance', \
                              'SwissFood', 'Architects', 'PartyBusRentals', 'Fondue', 'IrishPub', 'CookingSchools', \
                              'BespokeClothing', 'TaxServices', 'Matchmakers', 'Creperies', 'EasternGerman', 'International',\
                              'SprayTanning', 'MobilePhoneRepair', 'Brazilian', 'ValetServices', 'Churches', 'DanceSchools',\
                              'Rugs', 'Baden', 'SportsClubs', 'HotAirBalloons', 'DrywallInstallation&Repair', \
                              'FireProtectionServices', 'Guns&Ammo', 'AutoRepair', 'Cafes', 'Bagels', 'SurfShop', 'AmusementParks',\
                              'Vintage&Consignment', 'Clowns', 'ActiveLife', 'Archery', 'Tires', 'DrivingSchools', 'Lingerie', \
                              'Turkish', 'EmploymentAgencies', 'Bavarian', 'Chocolatiers&Shops', 'HomeWindowTinting', 'Bistros', \
                              'ChickenWings', 'GarageDoorServices', 'SelfStorage', 'Do-It-YourselfFood', 'OralSurgeons', \
                              'PublicTransportation', 'Beaches', 'Pubs', 'BoatDealers', 'Bartenders', 'WholesaleStores', \
                              'OsteopathicPhysicians', 'Doulas', 'Limos', 'AirportShuttles', 'Bookstores', 'Video/FilmProduction', \
                              'BuddhistTemples', 'Venezuelan', 'Hypnosis/Hypnotherapy', 'EthnicFood', 'Campgrounds', 'TruckRental', \
                              'Hospitals', 'CosmeticSurgeons', 'Accountants', 'MedicalTransportation', 'Painters', 'FastFood', \
                              'Reflexology', 'MortgageBrokers', 'Taxis', 'SecuritySystems', 'Gymnastics', 'BoatRepair', 'Mongolian', \
                              'Jewelry', 'Home&Garden', 'PetAdoption', 'ElementarySchools', 'HardwareStores', 'Waxing', 'InternetCafes',\
                              'Nurseries&Gardening', 'LeisureCenters', 'ChallengeCourses', 'PartySupplies', 'Hostels', 'RealEstateAgents',\
                              'Bowling', 'Halal', 'Music&Video', 'Paddleboarding', 'Cosmetics&BeautySupply', 'BikeSharing', \
                              'Videos&VideoGameRental', 'HealthMarkets', 'Breakfast&Brunch', 'FurnitureRepair', 'Colleges&Universities', \
                              'EthnicGrocery', 'Neurologist', 'BusTours', 'HorseBoarding', 'DimSum', 'Museums', 'InteriorDesign', \
                              'Carpeting', 'Cajun/Creole', 'PrintMedia', 'Heating&AirConditioning/HVAC', 'Barbeque', 'Cabinetry', 'Greek',\
                              'Party&EventPlanning', 'Ophthalmologists', 'Apartments', 'HookahBars', 'Buses', 'Flowers', 'Resorts', \
                              'Psychiatrists', 'Persian/Iranian', 'Flooring', 'Shades&Blinds', 'DiscountStore', 'Education', 'Veterinarians',\
                              'Glass&Mirrors', 'CannabisClinics', 'PostOffices', 'Airports', 'GolfEquipmentShops', 'Peruvian', 'Prosthetics',\
                              'Hotels&Travel', 'Trains', 'EducationalServices', 'Egyptian', 'RegistrationServices', 'Thai', 'Surgeons', \
                              'OilChangeStations', 'Landscaping', 'MailboxCenters', 'DUILaw', 'ScreenPrinting/T-ShirtPrinting', \
                              'PowderCoating', 'DogWalkers', 'Periodontists', 'DiagnosticImaging', 'PublicPlazas', 'MassageSchools', \
                              'Rheumatologists', 'SepticServices', 'RehabilitationCenter', 'Coffee&Tea', 'RealEstateLaw', \
                              'RefinishingServices', 'Pets', 'Cabaret', 'UrgentCare', 'Telecommunications', 'PermanentMakeup', 'Steakhouses',\
                              'Tex-Mex', 'MeatShops', 'ComedyClubs', 'Massage', 'Bridal', 'Piercing', 'Gastropubs', 'GolfEquipment', 'Wok',\
                              'RockClimbing', 'WindowsInstallation', 'Electronics', 'Mattresses', 'Orthopedists', 'TalentAgencies',\
                              'AnimalShelters', 'InternetServiceProviders', 'MeditationCenters', 'TapasBars', 'Watches', 'SummerCamps', \
                              'BankruptcyLaw', 'Playgrounds', 'Preschools', 'CarWash', 'HomeTheatreInstallation', 'NailSalons', 'BeerGardens', \
                              'Towing', 'Climbing', 'Vietnamese', 'PetBoarding/PetSitting', 'Hotels', 'ShippingCenters', 'Butcher', \
                              'Computers', 'Appliances', 'CPRClasses', 'RecyclingCenter', 'WeddingPlanning', 'Cuban', 'Pretzels', \
                              'MusicalInstrumentServices', 'WindshieldInstallation&Repair', 'American(New)', 'Firewood', 'SpecialEducation',\
                              'ModernEuropean', 'EventPlanning&Services', 'BootCamps', 'Donuts', 'Venues&EventSpaces', 'VapeShops', \
                              'Music&DVDs', 'Investing', 'TicketSales', 'TrampolineParks', 'FirstAidClasses', 'TutoringCenters', \
                              'Fences&Gates', 'CSA', 'Bed&Breakfast', 'Arabian', 'ElectronicsRepair', 'Indonesian', 'Wineries', \
                              'PoliceDepartments', 'MedicalSpas', 'Wine&Spirits', 'BatteryStores', 'Radiologists', 'Rolfing', \
                              'ShreddingServices', 'PoolHalls', 'DanceClubs', 'Photographers', 'TravelServices', 'RadioStations', \
                              'PhysicalTherapy', 'Pakistani', 'CarRental', 'Cambodian', 'AquariumServices', 'Restaurants', 'LocalFlavor', \
                              'SpecialtySchools', 'LegalServices', 'Fashion', 'LanguageSchools', 'MassMedia', 'HotDogs', 'HotTub&Pool',\
                              'SportsWear', 'Coffeeshops', 'Boxing', 'MakeupArtists', 'Courthouses', 'JewelryRepair', 'BubbleTea', \
                              'ChampagneBars', 'OutdoorGear', 'ComfortFood', 'Signmaking', 'Tattoo', 'GuestHouses', 'Roofing', 'RealEstateServices', \
                              'MiniGolf', 'MaternityWear', 'AsianFusion', 'ImmigrationLaw', 'PhotoBoothRentals', 'SkiResorts', \
                              'Himalayan/Nepalese', 'ArtClasses', 'Notaries', 'TrophyShops', 'German', 'Hats', 'PetGroomers', 'Polish', \
                              'FinancialAdvising', 'VideoGameStores', 'TestPreparation', 'EasternEuropean', 'Rafting/Kayaking', \
                              'CheckCashing/Pay-dayLoans', 'Brasseries', 'Arts&Entertainment', 'TattooRemoval', 'Psychics&Astrologers',\
                              'BrewingSupplies', 'Keys&Locksmiths', 'OfficeCleaning', 'PoleDancingClasses', 'Castles', 'TraditionalChineseMedicine',\
                              'Pita', 'Zoos', 'PawnShops', 'Dominican', 'BeerGarden', 'ShoppingCenters', 'Anesthesiologists', 'Automotive', \
                              'RealEstate', 'VacationRentals', 'DiveBars', 'Cafeteria', 'Spanish', 'VinylRecords', 'SwimmingLessons/Schools', \
                              'Antiques', 'PrivateInvestigation', 'Falafel', 'Cinema', 'WatchRepair', 'Orthodontists', 'Plumbing', 'PersonalChefs',\
                              'ComicBooks', 'PetServices', 'SkateParks', 'Uniforms', 'Laotian', 'ScubaDiving', 'ArtSupplies', 'Uzbek', 'PastaShops',\
                              'TrainStations', 'Sewing&Alterations', 'MotorcycleDealers', 'African', 'LightingFixtures&Equipment', \
                              'Gas&ServiceStations', 'GutterServices', 'LiceServices', 'Synagogues', 'FurnitureStores', 'Vegetarian', 'Lakes', \
                              'ShoeStores', 'CulturalCenter', 'Haitian', 'SkinCare', 'Chiropractors', 'Acupuncture', 'LaserTag', 'Framing',\
                              'HealthRetreats', 'Newspapers&Magazines', 'WalkingTours', 'PhotographyStores&Services', 'HinduTemples', \
                              'Dermatologists', 'DiagnosticServices', 'Teppanyaki', 'SeafoodMarkets', 'Lawyers', 'CarStereoInstallation', \
                              'ProfessionalSportsTeams', 'FormalWear', 'Counseling&MentalHealth', 'SoulFood', 'Australian', 'HomeDecor', 'Gyms',\
                              'HorsebackRiding', 'Cantonese', 'Gelato', 'Cardiologists', 'Insurance', 'OrganicStores', 'Handyman', 'Contractors', \
                              'RVRepair', 'MusicVenues', 'Fireworks', 'Shutters', 'TelevisionStations', 'CookingClasses', 'Women\'sClothing', \
                              'Florists', 'MotorcycleGear', 'Costumes', 'Stadiums&Arenas', 'Beer', 'Dentists', 'FamilyPractice', \
                              'LandscapeArchitects', 'Burmese', 'HorseRacing', 'LeatherGoods', 'MotorcycleRental', 'CurrencyExchange', \
                              'Mediterranean', 'Couriers&DeliveryServices', 'SpeechTherapists', 'Bars', 'Sugaring', 'BasketballCourts', 'Breweries', 'CarpetCleaning', 'MiddleEastern', 'Soccer', 'SecurityServices', 'Transportation', 'AmateurSportsTeams', 'Belgian', 'CurrySausage', 'Optometrists', 'TobaccoShops', 'LocalServices', 'JuiceBars&Smoothies', 'ChimneySweeps', 'HairExtensions', 'BartendingSchools', 'Desserts', 'Appliances&Repair', 'ToyStores', 'Wigs', 'Barbers', 'MobilePhones', 'Endocrinologists', 'Parks', 'PropertyManagement', 'FuneralServices&Cemeteries', 'SolarInstallation', 'Festivals', 'Indian', 'Jazz&Blues', 'Drugstores', 'WineBars', 'Kosher', 'Pharmacy', 'GiftShops', 'HomeStaging', 'JunkRemoval&Hauling', 'MusicalInstruments&Teachers', 'Colombian', 'Landmarks&HistoricalBuildings', 'Boating', 'Caterers', 'BarreClasses', 'RaceTracks', 'Cheesesteaks', 'BuildingSupplies', 'PublicServices&Government', 'SwimmingPools', 'Russian', 'Fish&Chips', 'Gastroenterologist', 'SportsMedicine', 'WindowWashing', 'SportsBars', 'PressureWashers', 'Kitchen&Bath', 'AdultEntertainment', 'Shopping', 'Singaporean', 'Walk-inClinics', 'Flowers&Gifts', 'Casinos', 'IceCream&FrozenYogurt', 'Salad', 'TreeServices', 'OfficeEquipment', 'Skydiving', 'GeneralLitigation', 'Austrian', 'Parking', 'Filipino', 'Fruits&Veggies', 'ShoeRepair', 'CustomizedMerchandise', 'Argentine', 'FoodTours', 'Aquariums', 'EmploymentLaw', 'Ukrainian', 'CosmeticDentists', 'YelpEvents', 'Banks&CreditUnions', 'HearingAidProviders', 'Nutritionists', 'HobbyShops', 'Psychologists', 'Hiking', 'PerformingArts', 'Naturopathic/Holistic', 'Vegan', 'EventPhotography', 'Portuguese', 'Mags', 'Cards&Stationery', 'Gun/RifleRanges', 'FoodCourt', 'FoodDeliveryServices', 'Afghan', 'Korean', 'ProfessionalServices', 'GraphicDesign', 'Karaoke', 'StreetVendors', 'Coffee&TeaSupplies', 'Beauty&Spas', 'British', 'BeerBar', 'Trinidadian', 'FarmersMarket', 'American(Traditional)', 'CyclingClasses', 'Lebanese', 'Mosques', 'Donairs', 'HomeCleaning', 'Used', 'Golf', 'ArtGalleries', 'Hawaiian', 'Pool&HotTubService', 'FirearmTraining', 'Pizza', 'Mexican', 'Lounges', 'CommunityService/Non-Profit', 'WineTours', 'LaboratoryTesting', 'Salvadoran', 'PetTraining', 'Surfing', 'ScreenPrinting', 'MassageTherapy', 'Southern', 'ThriftStores', 'Pediatricians', 'DepartmentStores', 'ReligiousOrganizations', 'Szechuan', 'PersonalAssistants', 'CarpetInstallation', 'Arts&Crafts', 'SerboCroatian', 'Embroidery&Crochet', 'Kebab', 'HomeInspectors', 'DryCleaning&Laundry', 'ArtSchools', 'Divorce&FamilyLaw', 'Malaysian', 'Oriental', 'MartialArts', 'PartyEquipmentRentals', 'GeneralFestivals', 'Obstetricians&Gynecologists', 'Bangladeshi', 'BlowDry/OutServices', 'SmogCheckStations', 'DanceStudios', 'ChristmasMarkets', 'AutoLoanProviders', 'SushiBars', 'PestControl', 'Audiologist', 'Swimwear', 'MountainBiking', 'HairSalons', 'Tennis', 'BikeRentals', 'DayCamps', 'Recording&RehearsalStudios', 'Oncologist', 'PianoServices', 'BodyShops', 'Tapas/SmallPlates', 'EstatePlanningLaw', 'CountryDanceHalls', 'WeightLossCenters', 'BusinessLaw', 'Opera&Ballet', 'TelevisionServiceProviders', 'Izakaya', 'HighFidelityAudioEquipment', 'Urologists', 'Iberian', 'Videographers', 'NannyServices', 'SportingGoods', 'Gardeners', 'Fertility', 'ConvenienceStores', 'Pulmonologist', 'StreetArt', 'Scottish', 'UniversityHousing', 'Health&Medical', 'Delis', 'Gluten-Free', 'TeaRooms', 'PrivateTutors', 'PersonalInjuryLaw', 'RVDealers', 'EyelashService', 'ReligiousSchools', 'Shanghainese', 'Delicatessen', 'PubFood', 'RVRental', 'DogParks', 'HomeOrganization', 'GeneralDentistry', 'Children\'sClothing', 'Live/RawFood', 'Scandinavian', 'Masonry/Concrete', 'Officiants', 'Men\'sHairSalons', 'ITServices&ComputerRepair', 'DoorSales/Installation', 'Poutineries', 'CollegeCounseling', 'PersonalShopping', 'BattingCages', 'DiscGolf', 'DJs', 'Burgers', 'Bakeries', 'Trainers', 'PayrollServices', 'AutoCustomization', 'Buffets', 'Libraries', 'SouvenirShops', 'SpecialtyFood', 'Bikes', 'CommercialRealEstate', 'AuctionHouses', 'CriminalDefenseLaw', 'SessionPhotography', 'PoolCleaners', 'PianoBars', 'Seafood', 'Hospice', 'French', 'Moroccan', 'RetirementHomes', 'FinancialServices', 'HomeServices', 'Caribbean', 'LaserHairRemoval', 'GayBars', 'CareerCounseling', 'TaiChi', 'GoldBuyers', 'RVParks', 'Italian', 'Yoga', 'FoodBanks', 'Books', 'Nightlife', 'Luggage', 'Chinese', 'Food', 'Movers', 'Tours', 'MedicalSupplies', 'CarDealers', 'FleaMarkets', 'Hungarian', 'Ethiopian', 'HairStylists']
                """
                print('\n Category head : {0}').format(len(categoryHead))
                header=['business_id','hours_Monday_open','hours_Monday_close','hours_Tuesday_open','hours_Tuesday_close',\
                          'hours_Wednesday_open','hours_Wednesday_close','hours_Thursday_open','hours_Thursday_close',\
                          'hours_Friday_open','hours_Friday_close','hours_Saturday_open','hours_Saturday_close',\
                          'hours_Sunday_open','hours_Sunday_close','attributes_Ambience_divey','attributes_Ambience_classy',\
                          'attributes_Ambience_touristy','attributes_Ambience_trendy','attributes_Ambience_intimate',\
                          'attributes_Ambience_casual','attributes_Ambience_romantic','attributes_Ambience_upscale',\
                          'attributes_Payment_Types_mastercard','attributes_Payment_Types_amex','attributes_Payment_Types_cash_only',\
                          'attributes_Payment_Types_discover','attributes_Payment_Types_visa','attributes_Accepts_Credit_Cards',\
                          'attributes_Good_For_brunch','attributes_Good_For_dinner','attributes_Good_For_breakfast',\
                          'attributes_Good_For_Kids','attributes_Good_For_dessert','attributes_Good_For_latenight',\
                          'attributes_Restrictions_vegan','attributes_Happy_Hour','attributes_Outdoor_Seating',\
                          'attributes_Alcohol','attributes_Parking_lot','attributes_Waiter_Service','attributes_Music_live',\
                          'attributes_Dietary_Restrictions_dairy_free','attributes_Music_background_music',\
                          'attributes_Parking_garage','review_count','attributes_Parking_valet',\
                          'attributes_Dietary_Restrictions_halal','attributes_Takes_Reservations','attributes_Delivery',\
                          'attributes_Wi_Fi','state','stars',\
                          'attributes_Price_Range',\
                          'attributes_Coat_Check',\
                          'attributes_Has_TV',\
                          'attributes_Dogs_Allowed','attributes_Drive_Thru','attributes_Dietary_Restrictions_vegetarian',\
                          'attributes_Noise_Level','attributes_Smoking','attributes_Attire']
                header.extend(categoryHead)
                #print('\n Len of header : {0}').format(len(header))
                businessVect.extend(header)
                #print('\n header : {0}').format(businessVect)
                tempDict['Header']=businessVect
                firstRow=False
            else:
                business_id=row[16]
                attributes_Ambience_divey=row[0]
                attributes_Restrictions_vegan=row[1]
                attributes_Happy_Hour=row[2]
                hours_Thursday_open=row[3]
                hours_Friday_open=row[8]
                attributes_Outdoor_Seating=row[11]
                attributes_Alcohol=row[12]
                attributes_Ambience_classy=row[13]
                attributes_Payment_Types_mastercard=row[14]
                attributes_Parking_lot=row[15]
                attributes_Ambience_touristy=row[17]
                hours_Tuesday_open=row[19]
                attributes_Good_For_brunch=row[20]
                attributes_Payment_Types_amex=row[21]
                hours_Monday_open=row[23]
                attributes_Waiter_Service=row[24]
                attributes_Music_live=row[29]
                attributes_Dietary_Restrictions_dairy_free=row[30]
                attributes_Music_background_music=row[31]
                attributes_Good_For_dinner=row[32]
                attributes_Good_For_breakfast=row[33]
                attributes_Parking_garage=row[34]
                review_count=row[37]
                state=row[39]
                attributes_Accepts_Credit_Cards=row[40]
                hours_Friday_close=row[41]
                attributes_Good_For_Kids=row[43]
                attributes_Parking_valet=row[44]
                hours_Thursday_close=row[47]
                attributes_Payment_Types_cash_only=row[49]
                attributes_Good_For_dessert=row[50]
                attributes_Dietary_Restrictions_halal=row[52]
                attributes_Takes_Reservations=row[53]
                hours_Saturday_open=row[54]
                attributes_Ambience_trendy=row[56]
                attributes_Delivery=row[57]
                hours_Wednesday_close=row[58]
                attributes_Wi_Fi=row[59]
                #city=row[61]
                attributes_Payment_Types_discover=row[62]
                stars=row[65]
                attributes_Payment_Types_visa=row[66]
                attributes_Ambience_intimate=row[69]
                attributes_Good_For_latenight=row[71]
                attributes_Price_Range=row[72]
                attributes_Coat_Check=row[73]
                hours_Monday_close=row[75]
                hours_Tuesday_close=row[77]
                hours_Saturday_close=row[78]
                hours_Sunday_open=row[81]
                attributes_Has_TV=row[85]
                hours_Sunday_close=row[86]
                attributes_Ambience_casual=row[87]
                attributes_Dogs_Allowed=row[90]
                attributes_Drive_Thru=row[91]
                attributes_Dietary_Restrictions_vegetarian=row[92]
                hours_Wednesday_open=row[93]
                attributes_Noise_Level=row[94]
                attributes_Smoking=row[95]
                attributes_Attire=row[96]
                attributes_Ambience_romantic=row[102]
                attributes_Ambience_upscale=row[104]

                #print('\n City : {0}').format(city)
                ## CategoytList
                catList=row[105:]
                print('\n Len of Category: {0}').format(len(catList))
                #print('\n catList : {0}').format(catList)

                ### Add all the attribute to tempList
                tempList=[business_id,hours_Monday_open,hours_Monday_close,hours_Tuesday_open,hours_Tuesday_close,\
                          hours_Wednesday_open,hours_Wednesday_close,hours_Thursday_open,hours_Thursday_close,\
                          hours_Friday_open,hours_Friday_close,hours_Saturday_open,hours_Saturday_close,\
                          hours_Sunday_open,hours_Sunday_close,attributes_Ambience_divey,attributes_Ambience_classy,\
                          attributes_Ambience_touristy,attributes_Ambience_trendy,attributes_Ambience_intimate,\
                          attributes_Ambience_casual,attributes_Ambience_romantic,attributes_Ambience_upscale,\
                          attributes_Payment_Types_mastercard,attributes_Payment_Types_amex,attributes_Payment_Types_cash_only,\
                          attributes_Payment_Types_discover,attributes_Payment_Types_visa,attributes_Accepts_Credit_Cards,
                          attributes_Good_For_brunch,attributes_Good_For_dinner,attributes_Good_For_breakfast,\
                          attributes_Good_For_Kids,attributes_Good_For_dessert,attributes_Good_For_latenight,\
                          attributes_Restrictions_vegan,attributes_Happy_Hour,attributes_Outdoor_Seating,\
                          attributes_Alcohol,attributes_Parking_lot,attributes_Waiter_Service,attributes_Music_live,\
                          attributes_Dietary_Restrictions_dairy_free,attributes_Music_background_music,\
                          attributes_Parking_garage,review_count,attributes_Parking_valet,\
                          attributes_Dietary_Restrictions_halal,attributes_Takes_Reservations,attributes_Delivery,\
                          attributes_Wi_Fi,state,stars,\
                          attributes_Price_Range,\
                          attributes_Coat_Check,\
                          attributes_Has_TV,\
                          attributes_Dogs_Allowed,attributes_Drive_Thru,attributes_Dietary_Restrictions_vegetarian,\
                          attributes_Noise_Level,attributes_Smoking,attributes_Attire]

                ## Append the categories to 'tempList'

                tempList.extend(catList)



                businessVect.extend(tempList)
                #print('\n Len of Row : {0}').format(len(businessVect))
                #print('\n businessVect : {0}').format(businessVect)
                tempDict[business_id]=businessVect
            #print('\n TempDict : {0}').format(tempDict)
        self.BusinessToCategory=tempDict

    def generateFeature(self,fileName,writeFile):
        """
        Desc : Master method for feature generation.

        """
        print('\n Feature Generation starts : ')
        #writeFile='/nobackup/anikgaik/search/features/Train_Features'
        BusinessToCategory=self.BusinessToCategory
        fr=csv.reader(open(fileName,'r'))
        firstRow=True
        feature=[]
        featureCount=0
        writeCount=0
        numberOfRows=0
        for row in fr:
            #featureCount+=1
            #if featureCount > 100000:
            #    break
            numberOfRows+=1

            if(firstRow):

                #print('\n Header : {0}').format(row)
                header=['user_id','business_id','day','month','year','votes_cool','votes_funny','votes_useful','label']
                #print('\n len of BusinessToCategory {0}').format(len(BusinessToCategory['Header']))
                header.extend(BusinessToCategory['Header'])
                feature.append(header)
                #print('\n len of header : {0}').format(len(header))
                firstRow=False
            else:
                # Header : ['user_id', 'review_id', 'text', 'votes.cool', 'business_id',
                # 'votes.funny', 'stars', 'date', 'type', 'votes.useful']
                dt=datetime.strptime(row[7],'%Y-%m-%d')
                month=dt.month
                day=dt.day
                year=dt.year
                user_id=row[0]
                votes_cool=int(row[3])
                business_id=row[4]
                votes_funny=int(row[5])
                votes_useful=int(row[-1])
                label=int(row[6])

                ### Get business info vetor
                business_vect=BusinessToCategory[business_id]
                #print('\n len of business_vect : {0}').format(len(business_vect))
                newRow=[user_id,business_id,day,month,year,votes_cool,votes_funny,votes_useful,label]
                newRow.extend(business_vect)

                feature.append(newRow)
                #if(business_id=='p_HFt0I92MHDNPWvdtyEBA' and user_id=='4AaaGtPaAPRwWijy5GYKwQ'):
                    #print('\n NewRow : {0}').format(feature[-1])
                #print('\n len of vector : {0}').format(len(feature))
                if(len(feature)>=1000):
                    writeCount+=1
                    self.writeFile(feature,writeFile)
                    feature=[]
        self.writeFile(feature,writeFile)
        #print('\n **** Expected records ***** : {0}').format(numberOfRows)
        #self.featureVector=feature

    def writeFile(self,data,fileName):
        """
        Desc : Write to file

        """
        #print('\n Writting File {0} : ').format(fileName)
        #fileName=self.dirName+"/"+fileName
        with open(fileName, 'ab') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(data)

'''
    def writeFile(self,fileName):
        print('\n Writting starts : ')
        #fileName=self.dirName+"/"+fileName
        with open(fileName, 'wb') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(self.featureVector)


'''



