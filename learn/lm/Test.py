#coding=gbk
import os
import jieba

line="�й��Ѿ��������仯��ᣬ�������˿�Լ�У��ڡ���ʪ�����ʪ�ؽ��ס������ס���׵�������������ȼ�������������������Ⱥ�����ڳ��������෢����������ʹ��֢����Լռ������Ⱥ��ģ�������������һȺ���������ڲ��ϵ����ӡ�"
# ���صĽṹ��һ���ɵ�����genertor
word_cut = jieba.cut(line, cut_all=False)
print (list(word_cut))
print (type(word_cut))