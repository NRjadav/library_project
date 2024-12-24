from django.shortcuts import render,HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Case, When, Value, IntegerField
# Create your views here.

def home(request):
    return HttpResponse("hello12345")


# ======================== Category =========================

      
class category_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = category.objects.get(id=id)
                serializer = category_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except category.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = category.objects.all().order_by("-id")
            """category.objects.annotate(
            sort_order=Case(
                When(number=0, then=Value(1)),  # Give a lower priority to 0 numbers
                default=Value(0),  # For other values, use priority 0
                output_field=IntegerField()
            )
        ).order_by("sort_order", "number", "-timestamp")"""
            serializer = category_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = category_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = category.objects.get(id=id)
        except category.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = category_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = category.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except category.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


# ======================== Author =========================

      
class author_view(APIView):
    def get(self, request, id=None , category_id=None ):
        if id:
            try:
                uid = author.objects.get(id=id)
                serializer = author_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except author.DoesNotExist:
                return Response({'status': "Invalid"})
        elif category_id:
            try:
                uid=author.objects.filter(category_data__id=category_id).order_by("-id")
                
                serializer=author_serializers(uid,many=True)
                print(len(serializer.data))
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})       
        else:
            uid = author.objects.all().order_by("-id")
            serializer = author_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = author_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = author.objects.get(id=id)
        except author.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = author_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = author.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except author.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})

# ======================== Languages =========================

      
class languages_view(APIView):
    def get(self, request, id=None , category_id=None ):
        if id:
            try:
                uid = Language.objects.get(id=id)
                serializer = Languages_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Language.DoesNotExist:
                return Response({'status': "Invalid"})
        elif category_id:
            try:
                uid=Language.objects.filter(category_data__id=category_id).order_by("-id")
                
                serializer=Languages_serializers(uid,many=True)
                print(len(serializer.data))
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})       
        else:
            uid = Language.objects.all().order_by("-id")
            serializer = Languages_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = Languages_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Language.objects.get(id=id)
        except Language.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = Languages_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Language.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Language.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})            

# ======================== User =========================

      
class user_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = user.objects.get(id=id)
                serializer = user_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except user.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = user.objects.all().order_by("-id")
            serializer = user_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = user_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = user.objects.get(id=id)
        except user.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = user_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = user.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except user.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


# ======================== Login User =========================

      
class login_user_view(APIView):
    def get(self, request, id=None,email=None):
        if id:
            try:
                uid = login_user.objects.get(user_id=id)
                serializer = login_user_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except login_user.DoesNotExist:
                return Response({'status': "Invalid"})
        elif email:
            try:
                uid = login_user.objects.get(email=email)
                serializer = login_user_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except login_user.DoesNotExist:
                return Response({'status': "Invalid"})        
        else:
            uid = login_user.objects.all().order_by("-id")
            serializer = login_user_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = login_user_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None,email=None):
        if id:
            try:
                uid = login_user.objects.get(user_id=id)
            except login_user.DoesNotExist:
                return Response({'status': "invalid data"})
            
            serializer = login_user_serializers(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        elif email:    
            try:
                uid = login_user.objects.get(email=email)
            except login_user.DoesNotExist:
                return Response({'status': "invalid data"})
            
            serializer = login_user_serializers(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = login_user.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except user.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


# ====================== Admin Login =======================
        
class admin_login_view(APIView):
    def get(self,request,id=None , email=None):

        if id:

            try:
                uid=admin_login.objects.get(id=id)
                serializer=admin_login_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid email"})
        elif email:

            try:
                uid=admin_login.objects.get(email=email)
                serializer=admin_login_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid email"})
        else:
            uid=admin_login.objects.all().order_by("-id")
            serializer=admin_login_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})

    def post(self,request):
            serializer=admin_login_serializers(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')

                uid=admin_login.objects.filter(email=email).exists()
                if uid:
                    uid=admin_login.objects.get(email=email)
                    if uid.password == password:
                        serializer=admin_login_serializers(uid)

                        return Response({'status':'success','data':serializer.data})
                    else:
                        return Response({'status':'invalid password'})
                else:
                    return Response({'status':'invalid email'})

            else:
                return Response({'status':"invalid data"})


    def patch(self,request,id=None):
        try:
            uid=admin_login.objects.get(id=id)
        except:
            return Response({'status':"invalid email"})
        serializer=admin_login_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid email"})
    def delete(self,request,id=None,email=None):
        if id:
            try:
                uid=admin_login.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        elif email:
            del request.session['email']
            return Response({'status': 'Logged out successfully'})

        else:
            return Response({'status':"invalid data"})
    def logout(self, request):
        try:
            del request.session['email']
        except KeyError:
            pass
        return Response({'status': 'Logged out successfully'})


# ========================= Book  ============================
      
class books_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Books.objects.get(id=id)
                serializer = BooksSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Books.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Books.objects.all().order_by("-id")
            serializer = BooksSerializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Books.objects.get(id=id)
        except Books.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = BooksSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Books.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Books.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


# ===================== Ad ===================
        

class ad_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = ad.objects.get(id=id)
                serializer = ad_serializers(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = ad.objects.order_by("-id")
            serializer = ad_serializers(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
        # pid=ad.objects.all()
        # pid.delete()
        serializer = ad_serializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data..."})



    def patch(self,request,id=None):

        if id:
            uid = ad.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = ad_serializers(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data..."})


    def delete(self,request,id=None):
        if id:
            try:
                uid = ad.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})


# ================== Notification ====================



class notification_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = notification.objects.get(id=id)
                serializer = NotificationSerializer(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = notification.objects.order_by("-id")
            serializer = NotificationSerializer(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
        # pid=Ad1.objects.all()
        # pid.delete()
        serializer = NotificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None):

        if id:
            uid = notification.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = NotificationSerializer(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = notification.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})

# ================== Hylighter ====================



class hylighter_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = hylighter.objects.get(id=id)
                serializer = HylighterSerializer(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = hylighter.objects.order_by("-id")
            serializer = HylighterSerializer(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
        # pid=Ad1.objects.all()
        # pid.delete()
        serializer = HylighterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None):

        if id:
            uid = hylighter.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = HylighterSerializer(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = hylighter.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})

# =========================== Add Cart Book ================    


class add_book_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = add_book.objects.get(id=id)
                serializer = Add_Book_Serializer(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = add_book.objects.order_by("-id")
            serializer = Add_Book_Serializer(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
      
        serializer = Add_Book_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None):

        if id:
            uid = add_book.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = Add_Book_Serializer(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = add_book.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})

# =========================== Add Book Wishlist ================    


class add_wishlist_book_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = wishlist.objects.get(id=id)
                serializer = Add_Wishlist_Book_Serializer(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = wishlist.objects.order_by("-id")
            serializer = Add_Wishlist_Book_Serializer(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
      
        serializer = Add_Wishlist_Book_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None):

        if id:
            uid = wishlist.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = Add_Wishlist_Book_Serializer(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = wishlist.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})




# ================== Hylighter ====================



class hylighter_view1(APIView):

    def get(self,request,id=None,user_id=None,book_id=None):

        if id:
            try:
                uid = hylighter1.objects.get(id=id)
                serializer = HylighterSerializer1(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})
        if user_id and book_id:
            try:
                uid = hylighter1.objects.get(user_data__user_id=user_id,book_data__id=book_id)
                serializer = HylighterSerializer1(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})    

        else:
            uid = hylighter1.objects.order_by("-id")
            serializer = HylighterSerializer1(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
        # pid=Ad1.objects.all()
        # pid.delete()
        serializer = HylighterSerializer1(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None,user_id=None,book_id=None):

        if id:
            uid = hylighter1.objects.get(id=id)
        elif user_id and book_id:    
            uid = hylighter1.objects.get(user_data__user_id=user_id,book_data__id=book_id)
        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = HylighterSerializer1(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = hylighter1.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})








class HylighterDeleteWordView(APIView):
    def get(self, request, user_id=None, book_id=None):
        try:
            # Get the user's highlighter data
            highlighter_data = hylighter1.objects.get(user_data__user_id=user_id, book_data__id=book_id)
            # Load the current 'words' field
            words_list = json.loads(highlighter_data.words)
            return Response({'status': 'success', 'words': words_list})
        except hylighter1.DoesNotExist:
            return Response({'status': 'error', 'message': 'User or book not found'})
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)})
    def delete(self, request, user_id=None,book_id=None, word_id=None):
        try:
            # Get the user's highlighter data (assuming you have a model for this, like `Hylighter1`)
            highlighter_data = hylighter1.objects.get(user_data__user_id=user_id,book_data__id=book_id)
            # Load the current 'words' field (assuming it is stored as a JSON string)
            words_list = json.loads(highlighter_data.words)
            print(words_list)

            # Find the word by its id and remove it
            word_to_delete = next((word for word in words_list if word.get('id') == word_id), None)
            
            if word_to_delete:
                words_list.remove(word_to_delete)  # Remove the word from the list

                # Save the updated words list back to the database
                highlighter_data.words = json.dumps(words_list)
                highlighter_data.save()

                return Response({'status': 'success', 'message': 'Word deleted successfully'})
            else:
                return Response({'status': 'error', 'message': 'Word not found'})

        except hylighter1.DoesNotExist:
            return Response({'status': 'error', 'message': 'User not found'})
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)})






























from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta
@api_view(['POST'])
def send_test_email(request):
    # Extract subject, message, and recipient from the request data
    subject = request.data.get('subject', 'Test Email')
    message = request.data.get('message', 'This is a test email sent from Django.')
    recipient = request.data.get('email', None)
    
    if recipient is None:
        return Response({"error": "Recipient email is required."})

    from_email = settings.EMAIL_HOST_USER

    # Render the HTML content from the template
    # html_content = render_to_string('email_template.html', {
    #     'subject': subject,
    #     'message': message
    # })
    
    try:
        send_mail(subject, message, from_email, [recipient]) #, html_message=html_content)
        uid=login_user.objects.get(email=recipient)
        uid.password_time=timezone.now() 
        uid.save()
        return Response({"success": "HTML email sent successfully!"})
    except Exception as e:
        return Response({"error": str(e)})
    





