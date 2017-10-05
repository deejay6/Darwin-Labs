from rest_framework.views import APIView
from django.http import JsonResponse
from models import User,SessionToken,Cart,CartPrdoduct
from django.contrib.auth.hashers import make_password, check_password


class VerifyUser(APIView):

    def get(self,request):
        try:
            result = []
            user_name = request.query_params['user_name']
            # For Verification of user , user can verify his/her identity either through email or from phone no.
            if user_name:
                while True:
                    try:
                        if int(user_name):
                            phone = user_name
                            user = User.objects.filter(phone=phone).first()
                            break
                    except:
                        email = user_name
                        user = User.objects.filter(email=email).first()
                        break
                if user:
                    message = "User Exists Proceed To LogIn"
                    user_details = {
                        'name': user.name,
                        'username': user.username
                        }
                    result.append(user_details)
                else:
                    message = "User Doesn't Exist. Please Register"

                response = {
                    'status':True,
                    'message':message,
                    'result':result
                    }
                return JsonResponse(response)
            else:
                response = {
                    'status': False,
                    'massage': "Invalid UserName",
                    'result':result
                    }
                return JsonResponse(response)
        except Exception as e:
            response = {
                'status':False,
                'message':'Error Occurred. Server Error'
                }
            return JsonResponse(response)


class Login(APIView):

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user:
            if check_password(password, user.password):
                token = SessionToken(user=user)
                token.create_token()
                token.save()
                response = {
                    'status': True,
                    'message': "Successfull Login"
                    }
                return JsonResponse(response)
            else:
                response = {
                    'status': False,
                    'message': "Invalid Password"
                    }
                return JsonResponse(response)
        else:
            response = {
                'status': False,
                'message': "Invalid Username"
                }
            return JsonResponse(response)


class Register(APIView):

    def post(self,request):
        try:
            name = request.data['name']
            username = request.data['username']
            email = request.data['email']
            phone = request.data['phone']
            gender = request.data['gender']
            password = request.data['password']
            age = request.data['age']
            user = User(name=name, username=username, email=email, phone=phone, gender=gender, age=age, password=make_password(password))
            user.save()
            cart = Cart(user_id=user.id)
            cart.save()
            response = {
                'status':True,
                'message': "User Added Successfully"
                }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'status': False,
                'message': 'Error Ocurred. Server Error'
                }
            return JsonResponse(response)


class AddToCart(APIView):
    def get(self,request):
        result = []
        try:
            cart_id = request.query_params['cart_id']
            product_id = request.query_params['product_id']
            catalogue_id = request.query_params['catalogue_id']
            add_to_cart = CartPrdoduct(cart_id=cart_id, product_id=product_id, catalogue_id=catalogue_id)
            add_to_cart.save()
            cart = Cart.objects.get(pk=cart_id)
            details = {
                'name': cart.user.name,
                'product': add_to_cart.product.name,
                'product_id': product_id
                }
            result.append(details)

            response = {
                'status':True,
                'message':"Product Added Successfully",
                'result':result
                }
            return JsonResponse(response)

        except Exception as e:
            response = {
                'status': False,
                'message': "Error Occurred . Server Error",
                'result': result
                }
            return JsonResponse(response)









