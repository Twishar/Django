from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(max_length=120)
    category = TreeForeignKey('Category', null=True,blank=True, on_delete=models.CASCADE)
    content = models.TextField('Content')
    slug = models.SlugField()

    def get_slug_list_for_categories(self):
        try:
            ancestors = self.category.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]

        slugs = []

        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))

        return slugs

    def __str__(self):
        return self.title


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    slug = models.SlugField()

    def _test(self):
        return self.get_descendants.cout()

    def _test2(self):
        sum = 0
        for val in self.get_descendants:
            sum += val.post_set.count()

        return sum

    test = property(_test)
    test_2 = property(_test2)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ('parent', 'slug',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
