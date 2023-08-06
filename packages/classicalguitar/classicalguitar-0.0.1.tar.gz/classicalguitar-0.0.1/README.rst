ทดสอบเขียนแพ็กเกจ Python ที่เกี่ยวกับ classicalguitar
=====================================================

Link: https://www.youtube.com/watch?v=8IEezGQwgZk

PyPi: https://pypi.org/project/classicalguitar/

สวัสดีจ้าาาา
แพ็คนี้คือแพ็คเกจที่อธิบายเรื่องราวเกี่ยวกับกีตาร์คลาสสิคแบบย่อๆ
โดยมีประวัติ การเล่นกีตาร์ และรูปภาพแอสกี

วิธีติดตั้ง
~~~~~~~~~~~

เปิด CMD / Terminal

.. code:: python

   pip install classicalguitar

วิธีใช้งานแพ็คเพจนี้
~~~~~~~~~~~~~~~~~~~~

-  เปิด IDLE ขึ้นมาแล้วพิมพ์…

.. code:: python

   from classicalguitar.classicgt import ClassicalGT

   gt = ClassicalGT()
   gt.show_name() #ทักทายกันหน่อย
   gt.show_youtube() #แสดงยูทูปการเล่นกีตาร์คลาสสิค
   gt.about() #รู้จักกับกีตาร์คลาสสิค
   gt.show_art() #แสดงภาพแอสกี

พัฒนาโดย: Doraeboy
