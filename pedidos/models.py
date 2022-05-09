from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=246, unique=True,)
    slug = models.SlugField(max_length=24, unique=True, help_text='The slug is the URL friendly version of the menu name, so that this can be accessed at a URL like mysite.com/menus/dinner/.')
    additional_text = models.CharField(max_length=128, null=True, blank=True, help_text='Any additional text that the menu might need, i.e. Served between 11:00am and 4:00pm.')
    order = models.PositiveSmallIntegerField(default=0, help_text='The order of the menu determines where this menu appears alongside other menus.')

    class Meta:
        verbose_name = 'menu name'

    def __str__(self):
        return self.name


"""
A Menu Category represents a grouping of items within a specific Menu.
An example of a Menu Category would be Appetizers, or Pasta.
"""


class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, null=True, help_text='The menus that this category belongs to, i.e. \'Lunch\'.', on_delete=models.SET_NULL)
    name = models.CharField(max_length=32, verbose_name='menu category name')
    additional_text = models.CharField(max_length=128, null=True, blank=True, help_text='The additional text is any bit of related information to go along with a menu category, i.e. the \'Pasta\' category might have details that say \'All entrees come with salad and bread\'.')
    order = models.IntegerField(default=0, help_text='The order is the order that this category should appear in when rendered on the templates.')

    class Meta:
        verbose_name = 'menu category'
        verbose_name_plural = 'menu categories'

    def __str__(self):
        return self.name


"""
A Menu Item is an item of food that the restaurant makes. A Menu Item can
belong to multiple Menu Categories to facilitate menus that have the same item
across multiple menus.
"""


class MenuItem(models.Model):
    CLASSIFICATION_CHOICES = (
        ('Burguers', 'burguers'),
        ('Hot dogs', 'hot dogs'),
        ('Papas locas', 'papas locas'),
    )

    name = models.CharField(max_length=48, help_text='Name of the item on the menu.')
    description = models.CharField(max_length=256, null=True, blank=True, help_text='The description is a simple text description of the menu item.')
    category = models.ManyToManyField(MenuCategory, blank=True, verbose_name='menu category', help_text='Category is the menu category that this menu item belongs to, i.e. \'Appetizers\'.')
    order = models.IntegerField(default=0, verbose_name='order', help_text='The order is to specify the order in which items show up on the menu.')
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text='The price is the cost of the item.')

    classification = models.CharField(max_length=20, choices=CLASSIFICATION_CHOICES, default=0, verbose_name='classification', help_text='Select if this item classifies as Vegetarian, Vegan, or Neither.')
    spicy = models.BooleanField(default=False, verbose_name='spicy?', help_text='Is this item spicy?')
    contains_peanuts = models.BooleanField(default=True, verbose_name='contain peanuts?', help_text='Does this item contain peanuts?')
    gluten_free = models.BooleanField(default=False, verbose_name='gluten free?', help_text='Is this item Gluten Free?')

    def menu_name(self):
        return ",".join([str(p) for p in self.category.all()])

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'
        verbose_name = 'menu name'

    def __str__(self):
        return self.name





















# class Usuario(models.Model):
#     login= models.CharField(max_length=30)
#     password=models.CharField(max_length=30)
#     email=models.CharField(max_length=60)
#     contact=models.CharField(max_length=10, help_text="Ingrese un número de contacto")


# class Pedido(models.Model):
#     fecha_pedido= models.DateTimeField("Hora del pedido")
#     contenido_pedido= models.CharField(max_length=200, help_text="Qué desea pedir?")
    
#     estatus_pedido=(
#         ('p', 'En preparación'),
#         ('e', 'Entregado'),
#     )

#     estatus= models.CharField(max_length=1, choices=estatus_pedido, blank=True,
#     default='p', help_text='Estatus del pedido')
#     usuarios_id= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.contenido_pedido

