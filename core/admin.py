from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin

from .models import Skill, TeamMember


class SkillInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'percentage', 'order')


@admin.register(TeamMember)
class TeamMemberAdmin(SortableAdminMixin, SortableAdminBase, admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'email')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'role', 'tagline')
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'member', 'percentage', 'order')
    list_filter = ('member',)
    list_editable = ('order', 'percentage')
