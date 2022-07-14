# # import numpy as np
# import base64
# import urllib
# from PIL import Image

# #Convert image to base64 thumbnail
# def img2base64(img_link):
#   with open("img_file.jpg", "wb") as f:
#       f.write(urllib.request.urlopen(img_link).read())
# #   tmp_img = np.asarray(Image.open("img_file.jpg"))
# #   tmp_thumb = tmp_img.resize((250, 250), Image.ANTIALIAS)
#   tmp_thumb.save("thumb_file.jpg")
#   with open("thumb_file.jpg", "rb") as img:
#     thumb_string = base64.b64encode(img.read())
#   base64out = "data:image/jpeg;base64," + str(thumb_string)[2:-1]
#   return(base64out)

a = "https://images.unsplash.com/photo-1541963463532-d68292c34b19?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8&w=1000&q=80"

import requests
import shutil
import base64
import uuid

# r = requests.get(a, stream=True)
# print("rr", r.text)
# with open("test2.png", 'wb') as f:
#     # r.raw.decode_content = True
#     print(r.raw)
#     b64_string = base64.b64encode(r.raw.read())
#     print(b64_string)
#     shutil.copyfileobj(r.raw, f)

# base64img =  base64.b64encode(requests.get(a).content)
# print(base64img)

gkyc_data = {
   "id":68,
   "gkyc_id":"50",
   "is_verified":False,
   "circuit_id":"50",
   "connect_id":"None",
   "smart_nid":"2383399413",
   "old_nid":"None",
   "driving_license":"None",
   "passport_no":"None",
   "name":"Md. Monir Hossan",
   "name_bn":"মোঃ মনির হোসেন",
   "spouse":"",
   "fathers_name":"Maqbool Ahmed",
   "fathers_name_bn":"মকবুল আহমদ",
   "mothers_name":"Peyara Akhter",
   "mothers_name_bn":"পেয়ারা আক্তার",
   "dob":"1996-12-10T00:00:00",
   "blood_group":"None",
   "gender":"male",
   "tin":"None",
   "permanent_address":"বাসা/হোল্ডিং: সওদাগার বাড়ী, গ্রাম/রাস্তা: কেগনা খিল, জয়াগ, ডাকঘর: পাঁচ বাড়িয়া-৩৮৬১, সোনাইমুড়ি, নোয়াখালী",
   "present_address":"Home / Holding: D 2/6, Village / Road: GEM Officers Colony, Ward No-40, Post Office: North Patenga-4204, Patenga, Chittagong",
   "verification_level":0,
   "photo":"https://prportal.nidw.gov.bd/file-9f/7/8/7/baaac9ce-4cf7-4036-b195-6233d797910e/Photo-baaac9ce-4cf7-4036-b195-6233d797910e.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=fileobj%2F20220706%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220706T113638Z&X-Amz-Expires=120&X-Amz-SignedHeaders=host&X-Amz-Signature=d6829e8a6b705b25f5d5c9f00fdb099628f26f7b8ada55f6c967a7d51fe1d558",
   "data":"{'transactionId': '0984c29a-b21f-4c3a-89bf-157e1c635737-O3cAgI3', 'creditCost': 2, 'creditCurrent': 832, 'status': 'YES', 'data': {'nid': {'fullNameEN': 'Md. Monir Hossan', 'fathersNameEN': 'Maqbool Ahmed', 'mothersNameEN': 'Peyara Akhter', 'presentAddressEN': 'Home / Holding: D 2/6, Village / Road: GEM Officers Colony, Ward No-40, Post Office: North Patenga-4204, Patenga, Chittagong', 'permenantAddressEN': 'Home / Holding: Merchant house, Village / Road: Kegna Khil, Jayag, Post Office: Panch Baria-361, Sonaimuri, Noakhali', 'fullNameBN': 'মোঃ মনির হোসেন', 'fathersNameBN': 'মকবুল আহমদ', 'mothersNameBN': 'পেয়ারা আক্তার', 'spouseNameBN': '', 'presentAddressBN': 'বাসা/হোল্ডিং: ডি ২/৭, গ্রাম/রাস্তা: জি ই এম অফিসার্স কলোনী, ওয়ার্ড নং-৪০, ডাকঘর: উত্তর পতেঙ্গা-৪২০৪, পতেঙ্গা, চট্টগ্রাম', 'permanentAddressBN': 'বাসা/হোল্ডিং: সওদাগার বাড়ী, গ্রাম/রাস্তা: কেগনা খিল, জয়াগ, ডাকঘর: পাঁচ বাড়িয়া-৩৮৬১, সোনাইমুড়ি, নোয়াখালী', 'gender': 'male', 'profession': 'ছাত্র/ছাত্রী', 'dateOfBirth': '1996-12-10T00:00:00', 'nationalIdNumber': '2383399413', 'oldNationalIdNumber': '19961596540000232', 'photoUrl': 'https://prportal.nidw.gov.bd/file-9f/7/8/7/baaac9ce-4cf7-4036-b195-6233d797910e/Photo-baaac9ce-4cf7-4036-b195-6233d797910e.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=fileobj%2F20220706%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220706T113638Z&X-Amz-Expires=120&X-Amz-SignedHeaders=host&X-Amz-Signature=d6829e8a6b705b25f5d5c9f00fdb099628f26f7b8ada55f6c967a7d51fe1d558'}}, 'errors': []}",
   "created_at":"2022-07-06T17:36:40.258251+06:00",
   "updated_at":"2022-07-06T17:36:40.258274+06:00"
}

# data  = gkyc_data["data"].replace("'", '"')

# print(data)


api = {
   "ENQUIRE_ACCOUNT_VALIDATION" : '/live/v7/Account/EnquireAccountValidation',
   "ENQUIRE_CUSTOMER" : '/live/v7/Customer/EnquireCustomer',
   "ENQUIRE_DEPOSIT_ACCOUNT" : '/live/v7/Account/EnquireDepositAccount',
   "ENQUIRE_CUSTOMER_LINKED_ACCOUNTS" : '/live/v7/Customer/EnquireCustomerLinkedAccounts',
   "ENQUIRE_LOAN_ACCOUNT" : '/live/v7/Account/EnquireLoanAccount',
   "ENQUIRE_FD_AND_RD_ACCOUNT" : '/live/v7/Account/EnquireFDAndRDAccount',
   "ENQUIRE_DEPOSIT_ONLINE_STATEMENT" : '/live/v7/Account/EnquireDepositOnlineStatement',
   "ENQUIRE_DEPOSIT_TRANSACTION" : '/live/v7/Account/EnquireDepositTransaction',
   "SINGLE_DEBIT_MULTI_CREDIT" : '/live/v7/Transaction/SingleDebitMultiCredit',
   "SINGLE_DEBIT_MULTI_CREDIT_CORRECTION" : '/live/v7/Transaction/SingleDebitMultiCreditCorrection',
   "ENQUIRE_LOAN_ONLINE_STATEMENT" : '/live/v7/Account/EnquireLoanOnlineStatement',
   "REPAY_LOAN_BY_TRANSFER" : '/live/v7/Loan/RepayLoanByTransfer',
   "ORDER_CHEQUE_BOOK" : '/live/v7/Cheque/ORDER_CHEQUE_BOOK',
   "FETCH_CHECKBOOK_STATUS" : '/live/v7/Cheque/FetchChequeBookStatus',
   "CREATE_CUSTOMER" : '/live/v7/Customer/CreateCustomer',
   "UPDATE_CUSTOMER" : '/live/v7/Customer/UploadCustomerDetails',
   "ENQUIRE_CCOD_ACCOUNT" : '/live/v7/Account/EnquireCCODAccount',
   "BEFTN_TRANSFER" : '/live/v7/BEFTN_RTGS/DebitNEFTByTransfer',
   "ENQUIRE_RTGS_BEFTN" : '/live/v7/BEFTN_RTGS/EnquireUTRForRTGSBEFTN',
   "CREATE_DEPOSITE_ACCOUNT" : '/live/v7/Account/CreateDepositAccount',
   "ENQUIRE_UUID" : '/live/v7/Transaction/EnquireUUID',
   "TRANSACTIONAL_PROFILE_CAPTURE" : '/live/v7/Transaction/TransactionProfileCapture'
}

account = {
   "CURRENT_ACCOUNT" : 'Current Account',
   "SAVINGS_ACCOUNT" : 'Saving Account',
   "SALARY_ACCOUNT" : 'Salary Account',
   "FIXED_DEPOSIT_ACCOUNT" : 'Fixed Deposit Account',
   "RECURRING_DEPOSIT_ACCOUNT" : 'Recurring Deposit Account',
   "NRI_ACCOUNT" : 'NRI Account',
   "NRO_SAVING_ACCOUNT" : 'NRO (Non-resident ordinary) Saving Account',
   "NRE_SAVING_ACCOUNT" : 'NRE (Non-resident external ) Saving Account',
   "FCNR_SAVING_ACCOUNT" : 'FCNR (Foreign currency non-resident) Account',
   "DEMAT_SAVING_ACCOUNT" : 'DEMAT (Dematerialized) Saving Account',
}

transactions = {
   "BKASH_TRAnSACTION" : 'BKASH Transaction',
   "NAGAD_TRANSACTION" : 'Nagag Transaction',
   "OK_WALLET_TRANSACTION" : 'OK Transaction',
   "TOP_UP" : 'Top Up',
   "BANGLALINK_TOP_UP" : 'Banglalink Link Top Up',
   "ROBI_TOP_UP" : 'Robi Top Up',
   "AIRTEL_TOP_UP" : 'Airtel Top Up',
   "GP_TOP_UP" : 'Grameenphone Top Up',
   "TELETALK_TOP_UP" : 'Teletalk Top Up',
   "BILL_PAY" : 'Bill Pay',
   "CREDIT_CARD_BILL_PAY" : 'Credit Card Bill Pay',
   "DPDC_BILL_PAY" : 'DPDC Bill Pay',
   "TITAS_BILL_PAY" : 'TITAS Bill Pay',
   "WASA_BILL_PAY" : 'WASA Bill Pay',
   "INTERNET_BILL_PAY" : 'Internet Bill Pay',
   "ADD_MONEY" : 'Add Money',
   "REQUEST_MONEY" : 'Request Money',
}

# for key , value in api.items():
#    with open('api_category.ts', 'a') as file:
#       file.write(f"""
#          [MiddlewareJblTcsServiceJblTcsApiCategories.{key}]: {{
#         id: '{uuid.uuid4()}',
#         name: '{key.replace('_', ' ').capitalize()}',
#         name_bn: '{key.replace('_', ' ').capitalize()}',
#         api_url : '{value}',
#         is_active: true,
#         deleted_at: null,
#       }},
#       """)
# for key , value in account.items():
#    with open('account_category.ts', 'a') as file:
#       file.write(f"""
#          [MiddlewareJblTcsServiceJblTcsAccountCategories.{key}]: {{
#         id: '{uuid.uuid4()}',
#         name: '{value}',
#         name_bn: '{value}',
#         is_active: true,
#         deleted_at: null,
#       }},
#       """)

for key , value in transactions.items():
   with open('transaction_category.ts', 'a') as file:
      file.write(f"""
         [MiddlewareJblTcsServiceJblTcsTransactionCategories.{key}]: {{
        id: '{uuid.uuid4()}',
        name: '{value}',
        name_bn: '{value}',
        is_active: true,
        deleted_at: null,
      }},
      """)