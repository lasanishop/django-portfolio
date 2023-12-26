from django.shortcuts import render


def home_view(request):
	context = {
		"title" : "Home"
	}
	return render(request, "home.html", context)


def ls_detail_view(request):
	context = {
		"title" : "Project Details"
	}
	return render(request, "projects/ls-detail.html", context)