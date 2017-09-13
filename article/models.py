from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import SiteManager
from django.utils import timezone
print(timezone.now())
# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __str__(self):
        return self.tag_name

class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(timezone.now())  #博客日期
    content = models.TextField(blank = True, null = True, default="")  #博客文章正文

    # 获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']


