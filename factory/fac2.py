# -*- coding: utf-8 -*-

# 工厂方法：定义一个接口来创建对象，但是创建对象由子类完成

from abc import ABC, abstractmethod
# 组件部分
class Section(ABC): 
    @abstractmethod 
    def describe(self): pass
class PersonalSection(Section): 
    def describe(self): print("PersonalSection")
class AlbumSection(Section): 
    def describe(self): print("AlbumSection")
class PatentSection(Section): 
    def describe(self): print("PatentSection")
class PublicationSection(Section): 
    def describe(self): print("PublicationSection")


# 工厂部分
class Profile(ABC): 
    def __init__(self): 
        self.sections = [] 
        self.create_profile() 
    @abstractmethod 
    def create_profile(self): pass 
    def show_sections(self): 
        for section in self.sections: 
            section.describe() 
    def add_section(self, section): 
        self.sections.append(section)
class LinkedIn(Profile): 
    def create_profile(self): 
        self.add_section(PersonalSection()) 
        self.add_section(PatentSection()) 
        self.add_section(PublicationSection())
class FaceBook(Profile): 
    def create_profile(self): 
        self.add_section(PersonalSection()) 
        self.add_section(AlbumSection())
if __name__ == '__main__': 
    linkedin = LinkedIn() 
    linkedin.show_sections() 
    """ PersonalSection PatentSection PublicationSection """ 
    facebook = FaceBook() 
    facebook.show_sections() 
    """ PersonalSection AlbumSection """
