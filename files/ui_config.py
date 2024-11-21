template_for_choosing = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>ChooseTheSubjects</class>
 <widget class="QMainWindow" name="ChooseTheSubjects">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>676</width>
    <height>558</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Привет</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>241</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>15</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Выберите предметы</string>
    </property>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>384</width>
      <height>501</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <widget class="QCheckBox" name="Math">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Математика</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="Russian">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Русский</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="English">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Английский</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="SecondForeign">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Немецкий</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="Literature">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Литература</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="History">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>История</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="SocialScience">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Обществознание</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="ClassHour">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Классный час</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="QCheckBox" name="PE">
         <property name="enabled">
          <bool>true</bool>
         </property>
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Физкультура</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="OBZR">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>ОБЗР</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="Chemistry">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Химия</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="Biology">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Биология</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="Physics">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Физика</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="Geography">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>География</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="IT">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Информатика</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QCheckBox" name="WAC">
         <property name="font">
          <font>
           <pointsize>12</pointsize>
          </font>
         </property>
         <property name="text">
          <string>МХК</string>
         </property>
         <property name="checked">
          <bool>true</bool>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">SubjectButtons</string>
         </attribute>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="ReadyButton">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>490</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Готово</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>0</y>
      <width>271</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>15</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Можете написать свои</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>30</y>
      <width>261</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>15</pointsize>
     </font>
    </property>
    <property name="text">
     <string>названия предметов</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>70</y>
      <width>251</width>
      <height>361</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="RemoveAll">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>15</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Убрать всё</string>
    </property>
   </widget>
   <widget class="QPushButton" name="SelectAll">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>15</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Выбрать всё</string>
    </property>
   </widget>
   <widget class="QLabel" name="LenErrorLabel">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>440</y>
      <width>261</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>11</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Ошибка: слишком длинные названия.</string>
    </property>
   </widget>
   <widget class="QLabel" name="SizeErrorLabel">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>465</y>
      <width>251</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>11</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Ошибка: слишком много названий.</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>676</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="SubjectButtons">
   <property name="exclusive">
    <bool>false</bool>
   </property>
  </buttongroup>
 </buttongroups>
</ui>
'''
