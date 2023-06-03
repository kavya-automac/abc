class AuthRouter:
    route_app_labels = {'auth', 'contenttypes','sessions','admin'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None

# class ABC:
#
#     route_app_labels = {'abcapp'}#app name
#
#     def db_for_read(self, model, **hints):
#         print('self',self)
#
#         if model._meta.app_label in self.route_app_labels:
#             print('model._meta',model._meta)
#             print('model._meta.app_label',model._meta.app_label)
#             print('self.route_app_labels',self.route_app_labels)
#             return 'abc_db'
#         return None
#
#     def db_for_write(self, model, **hints):
#
#         if model._meta.app_label in self.route_app_labels:
#             return 'abc_db'
#         return None
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#
#         if app_label in self.route_app_labels:
#             return db == 'abc_db'
#         return None



class ABC:
    route_app_labels = {'abcapp'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'demo_db' if model._meta.model_name == 'ABC' else 'abc_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'abc_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            if db == 'demo_db' or db == 'abc_db' :
                return True
        return None














class Demo:

    route_app_labels = {'demoapp'}

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'demo_db'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'demo_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'demo_db'
        return None


