from django.shortcuts import render,HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def home(request):
    return HttpResponse("hello1")


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
    def get(self, request, id=None):
        if id:
            try:
                uid = login_user.objects.get(id=id)
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

    def patch(self, request, id=None):
        try:
            uid = login_user.objects.get(id=id)
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


