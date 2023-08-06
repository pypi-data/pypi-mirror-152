แพ็คเกจนี้เป็นแพคเกจ python ที่โชว์ข้อมูลเกี่ยวกับคุณแคนดี้
===========================================================

PyPi: https://pypi.org/project/mynameiscandy/

สวัสดีจ้าาาา นี่คือแพ็คเกจที่แสดงข้อมูลเกี่ยวกับคุณแคนดี้
ทำเพื่อประกอบการเรียน python EP10 จ้า

วิธีติดตั้ง
~~~~~~~~~~~

เปิด CMD / Terminal

.. code:: python

   pip install mynameiscandy

วิธีใช้งานแพ็คเพจนี้
~~~~~~~~~~~~~~~~~~~~

-  เปิด IDLE ขึ้นมาแล้วพิมพ์…

.. code:: python

   from mynameiscandy import Candylady

   candy = Candylady() # ประกาศชื่อ class
   candy.show_name() # โชว์ชื่อ
   candy.show_youtube() # โชว์ลิงค์ youtube
   candy.about() # โชว์ลิงค์เพจเกี่ยวกับคุณแคนดี้
   candy.show_art() # โชว์ภาพศิลปะ

พัฒนาโดย: Candy Catja
