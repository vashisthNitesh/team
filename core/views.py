from django.views.generic import DetailView, ListView

from .models import TeamMember


class TeamMemberDetailView(DetailView):
    model = TeamMember
    template_name = 'core/member_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'member'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_members'] = TeamMember.objects.exclude(pk=self.object.pk)[:6]
        return context


class TeamListView(ListView):
    model = TeamMember
    template_name = 'core/member_list.html'
    context_object_name = 'members'
