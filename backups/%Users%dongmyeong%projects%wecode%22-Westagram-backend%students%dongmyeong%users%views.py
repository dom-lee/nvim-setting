Vim�UnDo� �uy������v6�`�Xt�п�Q�<z��   >   /                    nickname = data['nickname']      /                       `ڙ�    _�                     +        ����                                                                                                                                                                                                                                                                                                                                                             `ژ�     �   *   +          <<<<<<< HEAD5�_�                    ,        ����                                                                                                                                                                                                                                                                                                                                                             `ژ�     �   +   ,              1            if user.password != data['password']:5�_�                    ,        ����                                                                                                                                                                                                                                                                                                                            ,          :          V       `ژ�     �   +   ,          L                return JsonResponse({"message": "INVALID_USER"}, status=401)   5||||||| parent of be37e73 (Add: bcrypt & jwt feature)               if "email" in data:   W                user = User.objects.get(email=data['email'], password=data['password'])   !            elif "phone" in data:   W                user = User.objects.get(phone=data['phone'], password=data['password'])               else:   I                return JsonResponse({"message": "KEY_ERROR"}, status=401)   =======               if "email" in data:   <                user = User.objects.get(email=data['email'])   !            elif "phone" in data:   <                user = User.objects.get(phone=data['phone'])               else:                   raise KeyError5�_�                    1        ����                                                                                                                                                                                                                                                                                                                            ,          ,          V       `ژ�     �   0   1          +>>>>>>> be37e73 (Add: bcrypt & jwt feature)5�_�                    6        ����                                                                                                                                                                                                                                                                                                                            ,          ,          V       `ژ�     �   5   6          <<<<<<< HEAD5�_�                    9        ����                                                                                                                                                                                                                                                                                                                            9          @          V       `ژ�     �   8   9          5||||||| parent of be37e73 (Add: bcrypt & jwt feature)       =======               except KeyError:   E            return JsonResponse({"message": "KEY_ERROR"}, status=401)       +>>>>>>> be37e73 (Add: bcrypt & jwt feature)5�_�                            ����                                                                                                                                                                                                                                                                                                                                         
       V       `ژ�     �                import bcrypt   
import jwt5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                         
       V       `ژ�     �         6    �         6    5�_�      
           	   8        ����                                                                                                                                                                                                                                                                                                                            	          	   
       V       `ڙ     �   8                      �   8            5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                            	          	   
       V       `ڙ<     �         9      �            User.objects.create(email=data['email'], password=hashed_pw.decode('utf-8'), phone=data['phone'], nickname=data['nickname'])5�_�   
                    )    ����                                                                                                                                                                                                                                                                                                                            	          	   
       V       `ڙ@     �         :      |                    email=data['email'], password=hashed_pw.decode('utf-8'), phone=data['phone'], nickname=data['nickname'])5�_�                       8    ����                                                                                                                                                                                                                                                                                                                            	          	   
       V       `ڙE     �         ;      g                    password=hashed_pw.decode('utf-8'), phone=data['phone'], nickname=data['nickname'])5�_�                       )    ����                                                                                                                                                                                                                                                                                                                            	          	   
       V       `ڙK    �         <      C                    phone=data['phone'], nickname=data['nickname'])5�_�                       -    ����                                                                                                                                                                                                                                                                                                                            	          	   
       V       `ڙ�     �         =      .                    nickname=data['nickname'])5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       `ڙ�    �                -                    nickname=data['nickname']�                '                    phone=data['phone']�                6                    password=hashed_pw.decode('utf-8')�                (                    email=data['email'],5�_�                       8    ����                                                                                                                                                                                                                                                                                                                                                             `ڙ�     �         >      8                    password = hashed_pw.decode('utf-8')5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             `ڙ�     �         >      ,                    phone    = data['phone']5�_�                        /    ����                                                                                                                                                                                                                                                                                                                                                             `ڙ�    �         >      /                    nickname = data['nickname']5��