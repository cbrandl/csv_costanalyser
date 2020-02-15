# csv_costanalyser
Loading CSV files from banks and update categories


### Setup environment
pip install -r requirements.txt

### Start script
python csv_cleaner.py


### CSV Import Format
please see file csv_mapping.py for different mappings and formats

### CSV Export Format
- account_number
- account_name
- transaction_date
- value_date
- transaction_type
- booking_text
- amount
- currency
- original_amount
- original_currency
- company_name
- account_of_initiator
- bank_code_of_account_of_initiator
- IBAN_of_account_of_initiator
- category
- account_id
- created_at
- updated_at
- validated
- payee_id
- payee_name
- inbound
- outbound
- billing_date
- manipulationfee_in_eur
- used_exchange_rate
- statement_number
- transaction_timestamp
- revenue_text