from .fbv import (
    post_list, post_detail
)

from .post_view import (
    create_form,edit_form,delete_form,
    post_list_template, post_detail_template
)

from .user_view import (
    register, user_profile,
)

from .cbv import (
    UserDetailAPIView, UserListCreateAPIView,
)