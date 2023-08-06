สร้างไลบรารี Python อัพโหลดขึ้น PyPi.org แสดงข้อมูลเกี่ยวกับ ลุงช้าง
====================================================================

PyPi: https://pypi.org/project/mynameischang/

สวัสดี นี่คือ package ที่แสดงข้อมูลเกี่ยวกับลุงช้าง page link youtube
ได้

วิธีติดตั้ง
~~~~~~~~~~~

เปิด CMD / Terminal

.. code:: python

   pip install mynameischang

วิธีใช้งานแพ็คเพจนี้
~~~~~~~~~~~~~~~~~~~~

-  เปิด IDLE ขึ้นมาแล้วพิมพ์…

.. code:: python

   from mynameischang import Chang

   name = Chang() #ประกาศชื่อคลาส
   name.show_name() #โชว์ชื่อ
   name.show_page() #โชว์เพจ
   name.show_youtube() #โชว์ youtube
   name.about() #เกี่ยวกับ
   name.show_pic() #โชว์ภาพ ASCII

พัฒนาโดย: ลุงช้าง FB: https://www.facebook.com

YouTube: https://www.youtube.com
