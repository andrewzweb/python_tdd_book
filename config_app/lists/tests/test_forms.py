from django.test import TestCase
from lists.models import Item, List
from lists.forms import (
    DUPLICATE_ITEM_ERROR, EMPTY_ITEM_ERROR, 
    ExistingListItemForm, ItemForm
)

class ItemFormTest(TestCase):
    ''' test form form item '''
    
    def test_form_renders_item_text_input(self):
        ''' test input have arrt placeholder and ccs class'''
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_blank_items(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],[EMPTY_ITEM_ERROR])


    def test_form_save_handles_saving_to_a_list(self):
        '''test form save handles saving to a list'''
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='no twins!')
        form = ExistingListItemForm(for_list=list_, data={'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])





