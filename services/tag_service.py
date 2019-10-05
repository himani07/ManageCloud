from models.tag import Tag
from utils.exception import AppException
from utils.constants import exception_message
from datetime import datetime

class TagService:

    @staticmethod
    def get_tags():
        """
        Fetches all tags from db
        :return:
        """
        try:
            tags = Tag.get_all_tags()
        except:
            raise AppException(exception_message.get('CREATE_TAG_EXCEPTION'))
        tag_list = []
        dict_keys = ['tag_id', 'tag_key', 'tag_value', 'machine_id']
        for tag in tags:
            result_dict = dict(zip(dict_keys, tag))
            tag_list.append(result_dict)
        return tag_list

    @staticmethod
    def create_tag(input_data):
        try:
            Tag(input_data['tag_key'], input_data['tag_value'], input_data['machine_id'], is_deleted='N',
                created_by='himani.jain', created_timestamp=datetime.now()).save()
        except:
            raise AppException(exception_message.get('CREATE_TAG_EXCEPTION'))
        Tag.commit()
        return

    @staticmethod
    def delete_tag(input_data):
        try:
            tag_id = input_data['tag_id']
            Tag.delete(tag_id)
        except:
            raise AppException(exception_message.get('DELETE_TAG_EXCEPTION'))
        Tag.commit()
        return
