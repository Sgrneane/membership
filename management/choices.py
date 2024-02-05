#All choices field here 

MEMBERSHIP_TYPES=(
    (1,'General'),
    (2,'Institutional'),
    (3,'Lifetime'),
    (4,'Student'),
)
GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Others"))
DEGREE_TYPES=(("BE","Bachelor"),
              ("ME","Masters"),
              ("PHD","Phd"))

STUDENT_LEVEL_CHOICES = (("U", "Undergraduate"), ("P", "Postgraduate"))

SALUTATION_CHOICES = (
    ("P", "Prof"),
    ("D", "Dr"),
    ("E", "Er"),
    ("MR", "Mr"),
    ("MS", "Ms"),
)

COUNTRY_CHOICES = (
    ("AF", "Afghanistan"),
    ("AL", "Albania"),
    ("DZ", "Algeria"),
    ("AS", "American Samoa"),
    ("AD", "Andorra"),
    ("AO", "Angola"),
    ("AI", "Anguilla"),
    ("AQ", "Antarctica"),
    ("AG", "Antigua And Barbuda"),
    ("AR", "Argentina"),
    ("AM", "Armenia"),
    ("AW", "Aruba"),
    ("AU", "Australia"),
    ("AT", "Austria"),
    ("AZ", "Azerbaijan"),
    ("BS", "Bahamas"),
    ("BH", "Bahrain"),
    ("BD", "Bangladesh"),
    ("BB", "Barbados"),
    ("BY", "Belarus"),
    ("BE", "Belgium"),
    ("BZ", "Belize"),
    ("BJ", "Benin"),
    ("BM", "Bermuda"),
    ("BT", "Bhutan"),
    ("BO", "Bolivia"),
    ("BA", "Bosnia And Herzegovina"),
    ("BW", "Botswana"),
    ("BV", "Bouvet Island"),
    ("BR", "Brazil"),
    ("IO", "British Indian Ocean Territory"),
    ("BN", "Brunei Darussalam"),
    ("BG", "Bulgaria"),
    ("BF", "Burkina Faso"),
    ("BI", "Burundi"),
    ("KH", "Cambodia"),
    ("CM", "Cameroon"),
    ("CA", "Canada"),
    ("CV", "Cape Verde"),
    ("KY", "Cayman Islands"),
    ("CF", "Central African Republic"),
    ("TD", "Chad"),
    ("CL", "Chile"),
    ("CN", "China"),
    ("CX", "Christmas Island"),
    ("CC", "Cocos (Keeling) Islands"),
    ("CO", "Colombia"),
    ("KM", "Comoros"),
    ("CG", "Congo"),
    ("CD", "Congo, The Democratic Republic Of The"),
    ("CK", "Cook Islands"),
    ("CR", "Costa Rica"),
    ("CI", "Cote D'Ivoire"),
    ("HR", "Croatia"),
    ("CU", "Cuba"),
    ("CY", "Cyprus"),
    ("CZ", "Czech Republic"),
    ("DK", "Denmark"),
    ("DJ", "Djibouti"),
    ("DM", "Dominica"),
    ("DO", "Dominican Republic"),
    ("TP", "East Timor"),
    ("EC", "Ecuador"),
    ("EG", "Egypt"),
    ("SV", "El Salvador"),
    ("GQ", "Equatorial Guinea"),
    ("ER", "Eritrea"),
    ("EE", "Estonia"),
    ("ET", "Ethiopia"),
    ("FK", "Falkland Islands (Malvinas)"),
    ("FO", "Faroe Islands"),
    ("FJ", "Fiji"),
    ("FI", "Finland"),
    ("FR", "France"),
    ("GF", "French Guiana"),
    ("PF", "French Polynesia"),
    ("TF", "French Southern Territories"),
    ("GA", "Gabon"),
    ("GM", "Gambia"),
    ("GE", "Georgia"),
    ("DE", "Germany"),
    ("GH", "Ghana"),
    ("GI", "Gibraltar"),
    ("GR", "Greece"),
    ("GL", "Greenland"),
    ("GD", "Grenada"),
    ("GP", "Guadeloupe"),
    ("GU", "Guam"),
    ("GT", "Guatemala"),
    ("GN", "Guinea"),
    ("GW", "Guinea-Bissau"),
    ("GY", "Guyana"),
    ("HT", "Haiti"),
    ("HM", "Heard Island And Mcdonald Islands"),
    ("VA", "Holy See (Vatican City State)"),
    ("HN", "Honduras"),
    ("HK", "Hong Kong"),
    ("HU", "Hungary"),
    ("IS", "Iceland"),
    ("IN", "India"),
    ("ID", "Indonesia"),
    ("IR", "Iran, Islamic Republic Of"),
    ("IQ", "Iraq"),
    ("IE", "Ireland"),
    ("IL", "Israel"),
    ("IT", "Italy"),
    ("JM", "Jamaica"),
    ("JP", "Japan"),
    ("JO", "Jordan"),
    ("KZ", "Kazakhstan"),
    ("KE", "Kenya"),
    ("KI", "Kiribati"),
    ("KP", "Korea, Democratic People's Republic Of"),
    ("KR", "Korea, Republic Of"),
    ("KV", "Kosovo"),
    ("KW", "Kuwait"),
    ("KG", "Kyrgyzstan"),
    ("LA", "Lao People's Democratic Republic"),
    ("LV", "Latvia"),
    ("LB", "Lebanon"),
    ("LS", "Lesotho"),
    ("LR", "Liberia"),
    ("LY", "Libyan Arab Jamahiriya"),
    ("LI", "Liechtenstein"),
    ("LT", "Lithuania"),
    ("LU", "Luxembourg"),
    ("MO", "Macau"),
    ("MK", "Macedonia, The Former Yugoslav Republic Of"),
    ("MG", "Madagascar"),
    ("MW", "Malawi"),
    ("MY", "Malaysia"),
    ("MV", "Maldives"),
    ("ML", "Mali"),
    ("MT", "Malta"),
    ("MH", "Marshall Islands"),
    ("MQ", "Martinique"),
    ("MR", "Mauritania"),
    ("MU", "Mauritius"),
    ("YT", "Mayotte"),
    ("MX", "Mexico"),
    ("FM", "Micronesia, Federated States Of"),
    ("MD", "Moldova, Republic Of"),
    ("MC", "Monaco"),
    ("MN", "Mongolia"),
    ("MS", "Montserrat"),
    ("ME", "Montenegro"),
    ("MA", "Morocco"),
    ("MZ", "Mozambique"),
    ("MM", "Myanmar"),
    ("NA", "Namibia"),
    ("NR", "Nauru"),
    ("NP", "Nepal"),
    ("NL", "Netherlands"),
    ("AN", "Netherlands Antilles"),
    ("NC", "New Caledonia"),
    ("NZ", "New Zealand"),
    ("NI", "Nicaragua"),
    ("NE", "Niger"),
    ("NG", "Nigeria"),
    ("NU", "Niue"),
    ("NF", "Norfolk Island"),
    ("MP", "Northern Mariana Islands"),
    ("NO", "Norway"),
    ("OM", "Oman"),
    ("PK", "Pakistan"),
    ("PW", "Palau"),
    ("PS", "Palestinian Territory, Occupied"),
    ("PA", "Panama"),
    ("PG", "Papua New Guinea"),
    ("PY", "Paraguay"),
    ("PE", "Peru"),
    ("PH", "Philippines"),
    ("PN", "Pitcairn"),
    ("PL", "Poland"),
    ("PT", "Portugal"),
    ("PR", "Puerto Rico"),
    ("QA", "Qatar"),
    ("RE", "Reunion"),
    ("RO", "Romania"),
    ("RU", "Russian Federation"),
    ("RW", "Rwanda"),
    ("SH", "Saint Helena"),
    ("KN", "Saint Kitts And Nevis"),
    ("LC", "Saint Lucia"),
    ("PM", "Saint Pierre And Miquelon"),
    ("VC", "Saint Vincent And The Grenadines"),
    ("WS", "Samoa"),
    ("SM", "San Marino"),
    ("ST", "Sao Tome And Principe"),
    ("SA", "Saudi Arabia"),
    ("SN", "Senegal"),
    ("RS", "Serbia"),
    ("SC", "Seychelles"),
    ("SL", "Sierra Leone"),
    ("SG", "Singapore"),
    ("SK", "Slovakia"),
    ("SI", "Slovenia"),
    ("SB", "Solomon Islands"),
    ("SO", "Somalia"),
    ("ZA", "South Africa"),
    ("GS", "South Georgia And The South Sandwich Islands"),
    ("ES", "Spain"),
    ("LK", "Sri Lanka"),
    ("SD", "Sudan"),
    ("SR", "Suriname"),
    ("SJ", "Svalbard And Jan Mayen"),
    ("SZ", "Swaziland"),
    ("SE", "Sweden"),
    ("CH", "Switzerland"),
    ("SY", "Syrian Arab Republic"),
    ("TW", "Taiwan, Province Of China"),
    ("TJ", "Tajikistan"),
    ("TZ", "Tanzania, United Republic Of"),
    ("TH", "Thailand"),
    ("TG", "Togo"),
    ("TK", "Tokelau"),
    ("TO", "Tonga"),
    ("TT", "Trinidad And Tobago"),
    ("TN", "Tunisia"),
    ("TR", "Turkey"),
    ("TM", "Turkmenistan"),
    ("TC", "Turks And Caicos Islands"),
    ("TV", "Tuvalu"),
    ("UG", "Uganda"),
    ("UA", "Ukraine"),
    ("AE", "United Arab Emirates"),
    ("GB", "United Kingdom"),
    ("US", "United States"),
    ("UM", "United States Minor Outlying Islands"),
    ("UY", "Uruguay"),
    ("UZ", "Uzbekistan"),
    ("VU", "Vanuatu"),
    ("VE", "Venezuela"),
    ("VN", "Viet Nam"),
    ("VG", "Virgin Islands, British"),
    ("VI", "Virgin Islands, U.S."),
    ("WF", "Wallis And Futuna"),
    ("EH", "Western Sahara"),
    ("YE", "Yemen"),
    ("ZM", "Zambia"),
    ("ZW", "Zimbabwe"),
)

DISTRICT_CHOICES = (
    ('Taplejung', 'Taplejung'),
    ('Panchthar', 'Panchthar'),
    ('Ilam', 'Ilam'),
    ('Jhapa', 'Jhapa'),
    
    ('Morang', 'Morang'),
    ('Sunsari', 'Sunsari'),
    ('Dhankutta', 'Dhankutta'),
    ('Sankhuwasabha', 'Sankhuwasabha'),
    ('Bhojpur', 'Bhojpur'),
    ('Terhathum', 'Terhathum'),
    
    ('Okhaldunga', 'Okhaldunga'),
    ('Khotang', 'Khotang'),
    ('Solukhumbu', 'Solukhumbu'),
    ('Udaypur', 'Udaypur'),
    ('Saptari', 'Saptari'),
    ('Siraha', 'Siraha'),
    
    ('Dhanusa', 'Dhanusa'),
    ('Mahottari', 'Mahottari'),
    ('Sarlahi', 'Sarlahi'),
    ('Sindhuli', 'Sindhuli'),
    ('Ramechhap', 'Ramechhap'),
    ('Dolkha', 'Dolkha'),
    
    ('Sindhupalchauk', 'Sindhupalchauk'),
    ('Kavreplanchauk', 'Kavreplanchauk'),
    ('Lalitpur', 'Lalitpur'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Kathmandu', 'Kathmandu'),
    ('Nuwakot', 'Nuwakot'),
    ('Rasuwa', 'Rasuwa'),
    ('Dhading', 'Dhading'),
    
    ('Makwanpur', 'Makwanpur'),
    ('Rauthat', 'Rauthat'),
    ('Bara', 'Bara'),
    ('Parsa', 'Parsa'),
    ('Chitwan', 'Chitwan'),
    
    ('Gorkha', 'Gorkha'),
    ('Lamjung', 'Lamjung'),
    ('Tanahun', 'Tanahun'),
    ('Syangja', 'Syangja'),
    ('Kaski', 'Kaski'),
    ('Manag', 'Manag'),
    
    ('Mustang', 'Mustang'),
    ('Parwat', 'Parwat'),
    ('Myagdi', 'Myagdi'),
    ('Baglung', 'Baglung'),
    
    ('Gulmi', 'Gulmi'),
    ('Palpa', 'Palpa'),
    ('Nawalparasi', 'Nawalparasi'),
    ('Rupandehi', 'Rupandehi'),
    ('Arghakhanchi', 'Arghakhanchi'),
    ('Kapilvastu', 'Kapilvastu'),
    
    ('Pyuthan', 'Pyuthan'),
    ('Rolpa', 'Rolpa'),
    ('Western_Rukum', 'Western Rukum'),
    ('Eastern_Rukum', 'Eastern Rukum'),
    ('Salyan', 'Salyan'),
    ('Dang', 'Dang'),
    
    ('Bardiya', 'Bardiya'),
    ('Surkhet', 'Surkhet'),
    ('Dailekh', 'Dailekh'),
    ('Banke', 'Banke'),
    ('Jajarkot', 'Jajarkot'),
    
    ('Dolpa', 'Dolpa'),
    ('Humla', 'Humla'),
    ('Kalikot', 'Kalikot'),
    ('Mugu', 'Mugu'),
    ('Jumla', 'Jumla'),
    
    ('Bajura', 'Bajura'),
    ('Bajhang', 'Bajhang'),
    ('Achham', 'Achham'),
    ('Doti', 'Doti'),
    ('Kailali', 'Kailali'),
    
    ('Kanchanpur', 'Kanchanpur'),
    ('Dadeldhura', 'Dadeldhura'),
    ('Baitadi', 'Baitadi'),
    ('Darchula', 'Darchula')
)