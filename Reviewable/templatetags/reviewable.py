from django import template

register = template.Library()


@register.inclusion_tag('Reviewable/__review_controls.html', takes_context=True)
def show_review_controls(context, review_object):
    return {
        'review_count': review_object.review_count,
        'average_rating': review_object.average_rating,
        'content_type': review_object.content_type.model,
        'review_object': review_object
    }