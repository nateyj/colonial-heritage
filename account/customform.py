__author__ = 'Nate'

from django import forms


class CustomForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

# %for item in all_items:
# <div class="item_container text-center">
# <img src="${ STATIC_URL }catalog/media/product_images${ item.id }.jpg"/>
#             <div class="text-muted">${ item.name }</div>
#             <div class="text-center">
#                <button class="btn btn-xs btn-warning">Buy Now</button>
#             </div>
#         </div>
#     %endfor
