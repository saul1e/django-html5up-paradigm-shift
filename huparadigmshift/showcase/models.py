from django.db import models

# Create your models here.

class ModelSiteContents(models.Model):
    title = models.CharField(max_length=100, default="Current Set of Website Contents")

    # Section - Intro
    intro_headline = models.CharField(max_length=255, default="Paradigm Shift")
    intro_paragraph = models.TextField(default='''A free responsive site template designed by <a href="https://twitter.com/ajlkn">@ajlkn</a> / <a href="https://html5up.net">HTML5 UP</a>''')
    intro_img = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    # Section - First
    section_first_headline = models.CharField(max_length=255, default="Magna sed nullam nisl adipiscing")
    section_first_paragraph = models.TextField(default="<strong>Lorem ipsum dolor</strong> sit amet consectetur adipiscing elit. Duis dapibus rutrum facilisis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam tristique libero eu nibh porttitor amet fermentum. Nullam venenatis erat id vehicula ultrices sed ultricies condimentum. Magna sed etiam consequat, et lorem adipiscing sed nulla. Volutpat nisl et tempus et dolor libero, feugiat magna tempus, sed et lorem adipiscing.")
    section_first_img = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    # Section - Feature List
    section_generic_feature_list_headline = models.CharField(max_length=255, default="Feugiat consequat tempus ultrices")
    section_generic_feature_list_content =  models.TextField(default='''<p><strong>Etiam tristique libero</strong> eu nibh porttitor amet fermentum. Nullam venenatis erat id vehicula ultrices sed ultricies condimentum.</p>
	                                                                    <ul class="feature-icons">
	                                                                    	<li class="icon solid fa-laptop">Consequat tempus</li>
	                                                                    	<li class="icon solid fa-bolt">Etiam adipiscing</li>
	                                                                    	<li class="icon solid fa-signal">Libero nullam</li>
	                                                                    	<li class="icon solid fa-cog">Blandit condimentum</li>
	                                                                    	<li class="icon solid fa-map-marker-alt">Lorem ipsum dolor</li>
	                                                                    	<li class="icon solid fa-code">Nibh amet venenatis</li>
	                                                                    </ul>
	                                                                    <p>Vehicula ultrices sed ultricies condimentum. Magna sed etiam consequat, et lorem adipiscing sed nulla. Volutpat nisl et tempus et dolor libero, feugiat magna tempus, sed et lorem adipiscing.</p>''')
    # Section - Gallery
    
    section_gallery_main_headline = models.CharField(max_length=100,default='Ultrices erat magna sed condimentum')
    section_gallery_main_paragraph = models.TextField(default='<strong>Integer mollis egestas</strong> nam maximus erat id euismod egestas. Pellentesque sapien ac quam. Lorem ipsum dolor sit nullam.')
    
    section_gallery_secondary_headline = models.CharField(max_length=100,default='Erat aliquam')
    section_gallery_secondary_paragraph = models.TextField(default='Vehicula ultrices dolor amet ultricies et condimentum. Magna sed etiam consequat, et lorem adipiscing sed dolor sit amet, consectetur amet do eiusmod tempor incididunt  ipsum suspendisse ultrices gravida.')
    
    section_gallery_img_upper_landscape = models.ImageField(upload_to="projects/", blank=True, null=True)
    section_gallery_img_left_vertical = models.ImageField(upload_to="projects/", blank=True, null=True)
    section_gallery_img_right_vertical = models.ImageField(upload_to="projects/", blank=True, null=True)
    section_gallery_img_lower_landscape = models.ImageField(upload_to="projects/", blank=True, null=True)
    
    # Section - Buttons
    section_get_started_buttons_headline = models.CharField(max_length=100,default='Duis sed adpiscing veroeros amet')
    '''TODO: Vectorize button links and params'''
    section_get_started_buttons_paragraph = models.TextField(default='<strong>Proin tempus feugiat</strong> sed varius enim lorem ullamcorper dolore aliquam aenean ornare velit lacus, ac varius enim lorem ullamcorper dolore.')
    section_get_started_buttons_button_primary_text = models.CharField(max_length=100, default='Get Started')
    section_get_started_buttons_button_primary_link = models.URLField(default='http://localhost:8000 ')
    section_get_started_buttons_button_secondary_text = models.CharField(max_length=100, default='Learn More')
    section_get_started_buttons_button_secondary_link = models.URLField(default='http://localhost:8000 ')
    
    class Meta: 
        verbose_name = ("Site Contents Set")
        verbose_name_plural = ("Site Contents")
    
    def __str__(self):
        return self.title