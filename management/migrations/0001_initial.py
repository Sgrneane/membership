# Generated by Django 4.1 on 2024-02-06 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EducationalDocuments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "degree_type",
                    models.CharField(
                        choices=[("BE", "Bachelor"), ("ME", "Masters"), ("PHD", "Phd")],
                        max_length=3,
                    ),
                ),
                ("course", models.CharField(max_length=200)),
                ("institution", models.CharField(max_length=200)),
                ("university", models.CharField(max_length=200, null=True)),
                (
                    "country",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=2,
                    ),
                ),
                ("passed_year", models.CharField(max_length=4)),
                ("work_experience", models.TextField()),
                (
                    "educational_document",
                    models.FileField(null=True, upload_to="educational_document"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "membership_number",
                    models.CharField(max_length=10, null=True, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("verification", models.BooleanField(default=False)),
                ("expiry_date", models.DateField(blank=True, null=True)),
                (
                    "membership_since",
                    models.CharField(blank=True, max_length=4, null=True),
                ),
                ("verified_date", models.DateTimeField(blank=True, null=True)),
                ("rejected", models.BooleanField(default=False)),
                ("expiry_status", models.BooleanField(default=False)),
                (
                    "membership_type",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "General"),
                            (2, "Institutional"),
                            (3, "Lifetime"),
                            (4, "Student"),
                        ],
                        default=1,
                    ),
                ),
                ("remarks", models.TextField(null=True)),
                (
                    "associated_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="membership",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="NationalDocumment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identity_card_no", models.CharField(max_length=80)),
                ("dob", models.DateField()),
                (
                    "nationality",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=2,
                    ),
                ),
                ("identity_issued_from", models.CharField(max_length=150)),
                ("permanent_address", models.CharField(max_length=200)),
                (
                    "identity_card_image",
                    models.FileField(upload_to="identity_card_documents"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InstitutionalMembership",
            fields=[
                (
                    "membership_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="management.membership",
                    ),
                ),
                ("company_name", models.CharField(max_length=200)),
                ("company_address", models.CharField(max_length=200)),
                ("registration_no", models.CharField(max_length=200)),
                (
                    "pan_document",
                    models.FileField(null=True, upload_to="institutional_documents"),
                ),
                (
                    "registration_document",
                    models.FileField(null=True, upload_to="institutional_documents"),
                ),
                ("working_field", models.CharField(max_length=200, null=True)),
                ("contact_person", models.CharField(max_length=200, null=True)),
                ("contact_number", models.CharField(max_length=10, null=True)),
                ("website", models.CharField(max_length=250, null=True)),
                (
                    "logo",
                    models.ImageField(null=True, upload_to="institutional_documents"),
                ),
            ],
            bases=("management.membership",),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField()),
                ("paid", models.BooleanField(default=True)),
                ("payment_ss", models.FileField(null=True, upload_to="payment")),
                (
                    "paid_amount_in_paisa",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("pidx", models.CharField(blank=True, max_length=250, null=True)),
                ("txn_id", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "paypal_payer_id",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="paid_payment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to="management.membership",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentMembership",
            fields=[
                (
                    "membership_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="management.membership",
                    ),
                ),
                ("name_of_applicant", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        max_length=1,
                    ),
                ),
                ("affiliation", models.CharField(max_length=200)),
                ("pp_photo", models.ImageField(upload_to="personal_photo")),
                (
                    "salutation",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("P", "Prof"),
                            ("D", "Dr"),
                            ("E", "Er"),
                            ("MR", "Mr"),
                            ("MS", "Ms"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                ("phone_number", models.CharField(max_length=15, null=True)),
                (
                    "level",
                    models.CharField(
                        blank=True,
                        choices=[("U", "Undergraduate"), ("P", "Postgraduate")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("upgrade_request", models.BooleanField(null=True)),
                (
                    "educational_information",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="management.educationaldocuments",
                    ),
                ),
                (
                    "nationaldocument",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_membership",
                        to="management.nationaldocumment",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("management.membership", models.Model),
        ),
        migrations.CreateModel(
            name="GeneralMembership",
            fields=[
                (
                    "membership_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="management.membership",
                    ),
                ),
                ("name_of_applicant", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        max_length=1,
                    ),
                ),
                ("affiliation", models.CharField(max_length=200)),
                ("pp_photo", models.ImageField(upload_to="personal_photo")),
                (
                    "salutation",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("P", "Prof"),
                            ("D", "Dr"),
                            ("E", "Er"),
                            ("MR", "Mr"),
                            ("MS", "Ms"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                ("phone_number", models.CharField(max_length=15, null=True)),
                ("upgrade_request", models.BooleanField(null=True)),
                (
                    "educational_information",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="edu_members",
                        to="management.educationaldocuments",
                    ),
                ),
                (
                    "nationaldocument",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="associated_membership",
                        to="management.nationaldocumment",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("management.membership", models.Model),
        ),
    ]
