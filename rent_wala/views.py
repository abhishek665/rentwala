import json
import datetime
import pytz
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import strftime
from datetime import timedelta
from django.shortcuts import render, redirect
from .models import Cat, Product, User, PhoneOTP, UserInfo, MyUser, Order, ContactUs, GetOrder
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .serializer import CreateUserSerializer
import http.client
from . import forms
from twilio.rest import Client
from Crypto.PublicKey import RSA
import requests
import instaloader
import time


def insta(request):
    L = instaloader.Instaloader()

    posts = instaloader.Profile.from_username(L.context, "sewaliyamanish")

    for i in posts.get_posts():
        # print(L.format_filename(i, i.owner_username), i.owner_username)
        # filename = posts.username + '/' + L.format_filename(i, posts.username)
        L.download_post(i, target=posts.username)
        time.sleep(2)
# QsV-v483_X6mdbHWGkzSgaa36GPojwLWUjWNucyx
# user_credentials = ''
# def create_session():
#     key = RSA.generate(1024)
#     encrypted_key = key.export_key()
#     encrypted_key = str(encrypted_key)
#     encrypted_key = encrypted_key[50:150]
#     return encrypted_key

def send_sms(message, phone):
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=" + message + "&language=english&route=p&numbers=" + str(phone)
    headers = {
        'authorization': "Your_Key",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def send_email(reciever_mail, mail_cont):
    mail_content = mail_cont
    sender_address = '@gmail.com'
    sender_pass = '@1234'
    receiver_address = reciever_mail
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'RENTWALA'  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


conn = http.client.HTTPConnection('2factor.in')

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


def sess(request):
    user = []
    if request.session.get('_l*b7dx77!py+3i6to7r=*!vgtf(k*%i%w5-=1qq3&2s9ix#@_'):
        user_credential = request.session.get('_l*b7dx77!py+3i6to7r=*!vgtf(k*%i%w5-=1qq3&2s9ix#@_')
        phone = user_credential[0]
        name = user_credential[1]
        email = user_credential[2]
        profile_pic = user_credential[3]
        user = ["true", name, profile_pic, phone, email]
        return user
    else:
        return user


# Create your views here.
# @login_required(login_url='/log_in')
def manage_orders(request):
    user_sess = sess(request)
    if len(user_sess) < 5:
        return render(request, 'messages.html', {'messages': 'Session Expired. Please ', 'links': 'LogIn Again.'})
    phone = user_sess[3]
    user = MyUser.objects.get(phone=phone)
    main_orders = []
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    if len("a") == 1:
        user_order = Order.objects.filter(rel=user)
        user_orders = list(user_order.values())
        for i in user_orders:
            if not i['handshake']:
                expiry_date = i['return_date']
                time_left = expiry_date - current_time
                if time_left < timedelta(days=0, hours=0, minutes=0, milliseconds=0):
                    i['time_left'] = "Time To Return."
                else:
                    i['time_left'] = str(time_left)
                main_orders += [i]
        if len(main_orders) == 0:
            messages = "Sorry You Have No Orders"
            return render(request, 'messages.html', {'messages': messages})

        return render(request, 'manage_orders.html', {'orders': main_orders, 'user': user_sess})
    else:
        msg = "Invalid User"
        link = "Log In Again."
        return render(request, 'messages.html', {'messages': msg, 'links': link, 'user': user_sess})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home(request):
    # user_ip = get_client_ip(request)
    # ip = requests.get(f'http://api.ipstack.com/{user_ip}?access_key=')
    # new = json.loads(ip.text)
    # print(new['region_name'])
    user = sess(request)
    return render(request, 'home.html', {'user': user})
    # else:
    #     return redirect('/log_in')


# @login_required(login_url='/log_in')
def bucket(request, cat):
    user = sess(request)
    item = Cat.objects.filter(cat=cat)
    items = list(item.values())
    return render(request, 'bucket.html', {'items': items, 'cat': cat, 'user': user})
    # else:
    #     return render(request, 'login.html')


# @login_required(login_url='/log_in')
def bucketview(request, cat):
    user = sess(request)
    cats = cat.lower()
    item = Product.objects.filter(subcat=cats)
    items = list(item.values())
    return render(request, 'bucketview.html', {'items': items, 'cat': cat, 'user': user})
    # else:
    #     return render(request, 'login.html')


def item_view(request, sid):
    user = sess(request)
    item = Product.objects.filter(sid=sid)
    items = list(item.values())
    img = []
    n = 2
    for i in range(10, 12):
        if len(items[0]["Poster" + str(n)]) > 2:
            img += [items[0]["Poster" + str(n)]]
        n += 1
    return render(request, 'item_view.html', {'items': items, 'img': img, 'user': user, 'product_id': sid})
    # else:
    #     return render(request, 'login.html')


def log_in(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        passw = request.POST.get('password')
        users = MyUser.objects.filter(phone=phone)
        user = list(users.values())
        if len(user) == 1:
            checkpass = user[0]['password']
            names = user[0]['name']
            n = names.split(" ")
            name = n[0]
            email = user[0]['email']
            profile_pic = user[0]['profile_pic']
            if passw == checkpass:
                request.session['_l*b7dx77!py+3i6to7r=*!vgtf(k*%i%w5-=1qq3&2s9ix#@_'] = [phone, name, email, profile_pic]
                return redirect('/')
            else:
                messages = "Invalid Credentials. Please "
                links = "Try Again"
                return render(request, 'messages.html', {'messages': messages, 'links': links})
        else:
            messages = "False Credentials. Please "
            links = "Try Again"
            return render(request, 'messages.html', {'messages': messages, 'links': links})
    if request.session.get('_l*b7dx77!py+3i6to7r=*!vgtf(k*%i%w5-=1qq3&2s9ix#@_'):
        user_credential = request.session.get('_l*b7dx77!py+3i6to7r=*!vgtf(k*%i%w5-=1qq3&2s9ix#@_')
        phone = user_credential[0]
        user = MyUser.objects.get(phone=phone)
        if user:
            return redirect('/')
    else:
        return render(request, "login.html")


def log_out(request):
    logout(request)
    return redirect('/')


def order_id(phone):
    item = Order.objects.filter(phone=phone).last()
    spli = item.order_id.split('-')
    o = int(spli[1]) + 1
    odr_id = item.phone + '-' + str(o)
    return str(odr_id)


def get_orders(request):
    orders = Order.objects.filter(handshake=False)
    orderslst = list(orders.values())
    orderslstlen = len(orderslst)
    return_orders = []
    GetOrder.objects.all().delete()
    for i in range(0, orderslstlen):
        if not orderslst[i]['handshake']:
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            exd = orderslst[i]["return_date"]
            if current_time >= exd:
                phone = orderslst[i]['phone']
                name = orderslst[i]['name']
                address = orderslst[i]['address']
                quantity = orderslst[i]['quantity']
                days = orderslst[i]['days']
                time_left = orderslst[i]['time_left']
                title = orderslst[i]['title']
                total = orderslst[i]['total']
                order_id = orderslst[i]['order_id']
                product_id = orderslst[i]['product_id']
                poster = orderslst[i]['poster']
                validated = orderslst[i]['validated']
                return_date = orderslst[i]['return_date']
                date = orderslst[i]['date']
                out_for_delivery = orderslst[i]['out_for_delivery']
                received = orderslst[i]['received']
                delivered = orderslst[i]['delivered']
                handshake = orderslst[i]['handshake']
                myuser = MyUser.objects.get(phone=phone)
                getorder = GetOrder(phone=phone, rel=myuser, name=name, address=address, quantity=quantity, days=days,
                    time_left=time_left, title=title, total=total, order_id=order_id, product_id=product_id,
                    poster=poster, validated=validated, return_date=return_date, date=date, out_for_delivery=out_for_delivery,
                    received=received, delivered=delivered, handshake=handshake)
                getorder.save()
                return_orders += [orderslst[i]]
    # expiry_date = date + timedelta(hours=5, minutes=30) + timedelta(hours=time)
    # print(current_time.hour, current_time.minute)
    return HttpResponse(f"len of orders{len (return_orders)}{return_orders}")


def search(request):
    cat = request.GET.get('cat').lower()
    cats = Cat.objects.all()
    catlst = list(cats.values())
    catlen = len(catlst)
    category = []
    for i in range(0, catlen):
        title = catlst[i]["title"].lower()
        if cat in title:
            category += [[catlst[i]["title"]]]
    return HttpResponse(json.dumps(category))


def checkout(request):
    if request.POST:
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        ordr_id = order_id(phone)
        cat = request.POST.get('cat')
        name = request.POST.get('name')
        message = u"New Order Placed by {str(phone)} and order id is {str(ordr_id)} With Orders {str(cat)} at {str(" \
                  u"address)} by {str(name)} "
        send_sms(message, "8887896739")
        message = "We Have recieved Your request For Collecting Your " + str(cat) + "Scrab. We Will Reach you In An Hour."
        send_sms(message, phone)
        mail_cont = "New Order Placed by " + str(phone) + " and order id is " + str(ordr_id) + " With Orders " + str(
                 cat) + " at " + str(address) + " by " + str(name)
        send_email("storeforent@gmail.com", mail_cont)
        order = Order(name=name, phone=phone, address=address, order_id=ordr_id, category=cat)
        order.save()
        error_message = "Order Placed Successfully. Check your mail and Inbox. We Will Contact You Soon. "
        error_link = "Click here For Home"
        return render(request, 'messages.html', {'messages': error_message, 'return': error_link})
    return render(request, 'messages.html', {'messages': "Sorry Something Wrong Happened."})


def check(request):
    flag = []
    if request.session.get('_l*b7dx77!py+3i6to7r=*!vgtf(k*%i%w5-=1qq3&2s9ix#@_'):
        flag += ["true"]
        return HttpResponse(flag)
    else:
        flag += ["false"]
        return HttpResponse(flag)


def sign_up(request):
    return render(request, 'signup.html')


def user_info(request):
    return render(request, 'user_info.html')


def view_profile(request):
    user = sess(request)
    phone = user[3]
    user_profile = MyUser.objects.get(phone=phone)
    return render(request, 'view_profile.html', {'profile': user_profile, 'user': user})


def edit_profile(request):
    user = sess(request)
    phone = user[3]
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        MyUser.objects.filter(phone=phone).update(name=name, email=email, address=address)
        UserInfo.objects.filter(rel=MyUser.objects.get(phone=phone)).update(name=name, email=email, address=address)
        print(name, address, email, "saved")
        message = "Account updated Successfully."
        link = 'Return Home.'
        return render(request, 'messages.html', {'messages': message, 'home': link, 'user': user})
    user_profile = MyUser.objects.get(phone=phone)
    return render(request, 'edit_profile.html', {'profile': user_profile, 'user': user})


def change_password(request):
    if request.POST:
        user = sess(request)
        phone = user[3]
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            myuser = MyUser.objects.get(phone=phone)
            if myuser.password == current_password:
                MyUser.objects.filter(phone=phone).update(password=new_password)
                UserInfo.objects.filter(rel=myuser).update(password=new_password, password2=new_password)
                messages = "Password Changed Successfully."
                link = "Return Home"
                return render(request, 'messages.html', {'messages': messages, 'home': link})
            else:
                messages = "Current Password Didn`t Match."
                link = "Try Again"
                return render(request, 'messages.html', {'messages': messages, 'edit_profile': link})
        else:
            messages = "Passwords Dont Match. Please"
            link = "Try Again"
            return render(request, 'messages.html', {'messages': messages, 'edit_profile': link})
    else:
        messages = "Invalid Request. Return "
        link = "Home."
        return render(request, 'messages.html', {'messages': messages, 'links': link})


def contact_us(request):
    user = sess(request)
    if request.POST:
        querry = request.POST.get('desc')
        if len(querry) >= 30:
            myuser = MyUser.objects.get(phone=user[3])
            old_querry = ContactUs.objects.filter(rel=myuser).last()
            print(old_querry)
            mail_cont = str(querry) + " From " + str(user[3]) + " And His email Is " + str(user[4])
            if old_querry:
                print("entering Here.anf lund")
                querry_date = old_querry.date + timedelta(hours=24)
                current_date = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                if querry_date < current_date:
                    ContactUs(rel=myuser, querry=querry).save()
                    send_email("storeforentcontactus@gmail.com", mail_cont)
                    message = "Your Query Has Been Submitted Successfully. We Will Send You a Mail in Regard To Your " \
                              "Issues. It might Take Some Time. Return "
                    link = "Home"
                    return render(request, 'messages.html', {'messages': message, 'home': link, 'user': user})
                else:
                    message = "You Can Submit Only One querry in a Day. Return "
                    return render(request, 'messages.html', {'messages': message, 'home': "Home", 'user': user})
            else:
                print("entering Here.")
                myuser = MyUser.objects.get(phone=user[3])
                ContactUs(rel=myuser, querry=querry).save()
                send_email("storeforentcontactus@gmail.com", mail_cont)
                message = "Your Query Has Been Submitted Successfully. We Will Send You a Mail in Regard To Your " \
                          "Issues. It might Take Some Time. Return "
                link = "Home"
                return render(request, 'messages.html', {'messages': message, 'home': link, 'user': user})
        else:
            return render(request, 'messages.html', {'messages': "Sorry, Your Query Needs To Be More Descriptive", 'user': user})
    return render(request, 'contact_us.html', {'user': user})


def validate(request):
    phone_number = request.POST.get('phone')
    if len(phone_number) == 10:
        if phone_number:
            phone = str(phone_number)
            request.session['phone'] = phone
            user = MyUser.objects.filter(phone=phone)
            if user.exists():
                if request.POST.get('forgot_password'):
                    phone_number = request.POST.get('forgot_phone')
                    phone = str(phone_number)
                    key = send_otp(phone)
                    if key:
                        old = PhoneOTP.objects.filter(phone__iexact=phone)
                        if old.exists():
                            old = old.first()
                            count = old.count
                            # key = old.otp
                            PhoneOTP.objects.filter(phone__iexact=phone).delete()
                            obj = PhoneOTP.objects.create(
                                phone=phone,
                                otp=key,
                                count=count,
                            )
                            obj.save()
                            old = PhoneOTP.objects.filter(phone__iexact=phone)
                            old = old.first()
                            if count > 5:
                                return HttpResponse("Limit Exceeded")
                            else:
                                old.count = count + 1
                                old.save()
                                message = "Your Password Reset OTP Is " + str(key)
                                send_sms(message, phone)
                                # message = client.messages \
                                #     .create(
                                #     body="Your Password Reset OTP Is " + str(key),
                                #     from_='+15014303402',
                                #     to='+91' + phone
                                # )
                                return HttpResponse("Sent Successfully")
                        else:
                            obj = PhoneOTP.objects.create(
                                phone=phone,
                                otp=key,
                            )
                            obj.save()
                            try:
                                message = "Your Password Reset OTP Is " + str(key)
                                send_sms(message, phone)
                                # message = client.messages \
                                #     .create(
                                #     body="Your Password Reset OTP Is " + str(key),
                                #     from_='+15014303402',
                                #     to='+91' + phone
                                # )
                            except Exception as e:
                                print(e)
                            return HttpResponse("Sent Successfully")
                else:
                    return HttpResponse("User Exists")
            else:
                key = send_otp(phone)
                if key:
                    old = PhoneOTP.objects.filter(phone__iexact=phone)
                    if old.exists():
                        old = old.first()
                        count = old.count
                        # key = old.otp
                        PhoneOTP.objects.filter(phone__iexact=phone).delete()
                        obj = PhoneOTP.objects.create(
                            phone=phone,
                            otp=key,
                            count=count,
                        )
                        obj.save()
                        old = PhoneOTP.objects.filter(phone__iexact=phone)
                        old = old.first()
                        if count > 5:
                            return HttpResponse("Limit Exceeded")
                        else:
                            old.count = count + 1
                            old.save()
                            message = "Your OTP Is " + str(key)
                            send_sms(message, phone)
                            # message = client.messages \
                            #     .create(
                            #     body="Your OTP Is " + str(key),
                            #     from_='+15014303402',
                            #     to='+91' + phone
                            # )
                            return HttpResponse("Sent Successfully")
                    else:
                        obj = PhoneOTP.objects.create(
                            phone=phone,
                            otp=key,
                        )
                        obj.save()
                        try:
                            message = "Your OTP Is " + str(key)
                            send_sms(message, phone)
                            # message = client.messages \
                            #     .create(
                            #     body="Your OTP Is " + str(key),
                            #     from_='+15014303402',
                            #     to='+91' + phone
                            # )
                        except Exception as e:
                            print(e)
                        return HttpResponse("Sent Successfully")
                else:
                    return HttpResponse("OTP Sending Error")
        else:
            return HttpResponse("No Phone Number Provided")
    else:
        return HttpResponse("Invalid Phone Length")


def ValidateOTP(request):
    phone = request.session.get('phone')
    otp_sent = request.POST.get('otp')
    if otp_sent and phone:
        old = PhoneOTP.objects.filter(phone=phone)
        if old.exists():
            old = old.first()
            otp = old.otp
            otp_time = old.date
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            if current_time > otp_time + timedelta(minutes=1):
                return HttpResponse('OTP Expired')
            if str(otp_sent) == str(otp):
                old.validated = True
                old.save()
                if request.POST.get('forgot_password'):
                    MyUser.objects.filter(phone=phone).update(password=str(otp_sent) + "123")
                    UserInfo.objects.filter(rel=MyUser.objects.get(phone=phone)).update(password=str(otp_sent) + "123",
                                                                                        password2=str(otp_sent) + "123")
                    message = "Your Password Is " + str(otp_sent) + "123 . Please Change It Immediately."
                    send_sms(message, phone)
                    # message = client.messages \
                    #     .create(
                    #     body="Your Password Is " + str(otp_sent) + "123 . Please Change It Immediately.",
                    #     from_='+15014303402',
                    #     to='+91' + phone
                    # )
                    messages = "We Have sent Your Password On Your Registered Phone. Please Change It Immediately. "
                    links = "LogIn To Change."
                    return HttpResponse("Success")
                return HttpResponse("success")
            else:
                return HttpResponse("OTP Incorrect")
        else:
            return HttpResponse("Send Otp First")
    else:
        return HttpResponse("Please Provide Phone and OTP.")


def Register(request):
    phone = request.session.get('phone')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    address = request.POST.get('address')
    email = request.POST.get('email')
    aadhar = request.FILES.get('aadhar')
    dp = request.FILES.get('dp')
    pan = request.FILES.get('pan')
    name = request.POST.get('full_name')
    if phone and password:
        if password == password2:
            old = PhoneOTP.objects.filter(phone__iexact=phone)
            if old.exists():
                old = old.first()
                validated = old.validated
                if validated:
                    myuser = MyUser(phone=phone, password=password, name=name, email=email, profile_pic=dp)
                    myuser.save()
                    inst = MyUser.objects.get(phone=phone)
                    newuser = UserInfo(rel=inst, password2=password2, phone=phone, password=password, email=email,
                                       address=address, aadhar_card=aadhar, pan_card=pan, name=name, profile_pic=dp)
                    newuser.save()
                    try:
                        message = "New User Register with phone" + " " + str(phone) + "."
                        send_sms(message, "8887896739")
                        # message = client.messages \
                        #     .create(
                        #     body="New User Register with phone" + " " + str(phone) + ".",
                        #     from_='+15014303402',
                        #     to='+918887896739'
                        # )
                    except Exception as e:
                        print(e)
                    error_message = "Account Created Successfully. CliCk Here For "
                    error_link = "Log In"
                    return render(request, 'messages.html', {'messages': error_message, 'links': error_link})
                else:
                    error_message = "Phone Hav not Verified yet via OTP. Please Complete That Process First."
                    return render(request, 'messages.html', {'messages': error_message})
            else:
                error_message = "Please Verify Your Phone First. "
                error_link = 'Verify Here'
                return render(request, 'messages.html', {'messages': error_message, 'links': error_link})
    else:
        error_message = "Phone Or Password Details Are Not Filled Correctly. "
        error_link = "Try Again"
        return render(request, 'messages.html', {'messages': error_message, 'links': error_link})


def send_otp(phone):
    if phone:
        key = random.randint(111111, 999999)
        return key
    else:
        return False
