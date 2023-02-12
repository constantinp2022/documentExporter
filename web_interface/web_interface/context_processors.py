
from user.models import Profile
from posts.models import Post
from default_tmpl.models import Default_Templates
from django.db.models import Sum

def global_stats(request):
    return {
		'nr_users': Profile.objects.count(),
		'nr_templates': Default_Templates.objects.count(),
		'nr_posts' :  Post.objects.count(),
		'nr_documents' : Profile.objects.aggregate(Sum('nr_documents'))['nr_documents__sum']
	}