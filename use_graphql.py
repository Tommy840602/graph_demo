import graphene

class User(graphene.ObjectType):
    id = graphene.Int()         
    name = graphene.String()   
    age = graphene.Int()       

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int())
    
    def resolve_user(self, info, id):
        users = {
            1: {"id": 1, "name": "Alice", "age": 30},
            2: {"id": 2, "name": "Bob", "age": 25},
        }
        return users.get(id, None)

schema = graphene.Schema(query=Query)

query_string = '''
    query getUser($id: Int) {
        user(id: $id) {
            id
            name
            age
        }
    }
'''

result = schema.execute(query_string, variable_values={"id": 1})
print(result.data)