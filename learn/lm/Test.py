#coding=gbk
import os
import jieba

line="中国已经步入老龄化社会，中老年人口约有５亿。风湿和类风湿关节炎、肩周炎、颈椎病、骨质增生等疾病在老年甚至中年人群中属于常见病、多发病，各类疼痛病症患者约占中老年群体的６５％，而且这一群体数量还在不断的增加。"
# 返回的结构是一个可迭代的genertor
word_cut = jieba.cut(line, cut_all=False)
print (list(word_cut))
print (type(word_cut))