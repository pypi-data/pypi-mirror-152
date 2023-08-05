import json
from typing import Dict,Optional
from localstack.services.cloudformation.service_models import(REF_ARN_ATTRS,REF_ID_ATTRS,GenericBaseModel)
from localstack.utils.aws import aws_stack
from localstack.utils.common import clone,keys_to_lower,select_attributes,to_str
from localstack_ext.services.appsync import appsync_api
from localstack_ext.services.cloudformation.service_models import LOG
from localstack_ext.utils.aws import aws_utils
class AppSyncResolver(GenericBaseModel):
 @staticmethod
 def cloudformation_type():
  return "AWS::AppSync::Resolver"
 def get_physical_resource_id(self,attribute,**kwargs):
  if attribute in REF_ID_ATTRS:
   return self.props.get("resolverArn")
 def fetch_state(self,stack_name,resources)->Optional[Dict]:
  props=self.props
  api_id=props.get("ApiId")
  type_name=props.get("TypeName")
  field_name=props.get("FieldName")
  data_source_name=props.get("DataSourceName")
  return self.fetch_details(api_id,type_name,field_name,data_source_name)
 @classmethod
 def fetch_details(cls,api_id,type_name,field_name,data_source_name)->Optional[Dict]:
  client=aws_stack.connect_to_service("appsync")
  resolvers=client.list_resolvers(apiId=api_id,typeName=type_name)["resolvers"]
  result=[r for r in resolvers if r.get("fieldName")==field_name and r.get("dataSourceName")==data_source_name]
  return(result or[None])[0]
 def update_resource(self,new_resource,stack_name,resources):
  client=aws_stack.connect_to_service("appsync")
  new_props=new_resource["Properties"]
  current_state=self.fetch_state(stack_name,resources)
  if not current_state:
   return
  attrs=set(current_state.keys())|set(new_props.keys())
  attrs=[attr for attr in attrs if attr not in["apiId","resolverArn"]]
  if all(new_props.get(attr)==current_state.get(attr)for attr in attrs):
   return
  params=self._get_resolver_params(new_props)
  return client.update_resolver(**params)
 @classmethod
 def get_deploy_templates(cls):
  return{"create":{"function":"create_resolver","parameters":cls._get_resolver_params},"delete":{"function":"delete_resolver","parameters":{"apiId":"ApiId","typeName":"TypeName","fieldName":"FieldName"}}}
 @staticmethod
 def _get_resolver_params(props,**kwargs):
  params=keys_to_lower(clone(props))
  req_template=params.pop("requestMappingTemplateS3Location",None)
  res_template=params.pop("responseMappingTemplateS3Location",None)
  if req_template:
   tmpl=aws_utils.download_s3_object(req_template,as_str=True)
   if tmpl:
    params["requestMappingTemplate"]=tmpl
  if res_template:
   tmpl=aws_utils.download_s3_object(res_template,as_str=True)
   if tmpl:
    params["responseMappingTemplate"]=tmpl
  return params
class GraphQLSchema(GenericBaseModel):
 @staticmethod
 def cloudformation_type():
  return "AWS::AppSync::GraphQLSchema"
 def get_physical_resource_id(self,attribute,**kwargs):
  return "%s-GraphQLSchema"%self.props.get("ApiId")
 @classmethod
 def fetch_details(cls,api_id,definition=None,s3_location=None):
  client=aws_stack.connect_to_service("appsync")
  try:
   schema=client.get_introspection_schema(apiId=api_id,format="SDL")["schema"]
   schema=schema.read()if hasattr(schema,"read")else schema
   schema=to_str(schema)
   if schema.startswith("{"):
    schema=json.loads(schema)["schema"]
   if definition:
    if to_str(definition).strip()==to_str(schema).strip():
     return{"schema":definition}
   elif s3_location:
    LOG.debug("Getting GraphQL schema definition from S3 not yet implemented")
    return{"schema":definition}
  except Exception:
   pass
class AppSyncApiKey(GenericBaseModel):
 @staticmethod
 def cloudformation_type():
  return "AWS::AppSync::ApiKey"
 def get_cfn_attribute(self,attribute_name):
  if attribute_name=="ApiKey":
   return self._get_key_id()
  if attribute_name in REF_ID_ATTRS+REF_ARN_ATTRS:
   return self.get_physical_resource_id()
  return super(AppSyncApiKey,self).get_cfn_attribute(attribute_name)
 def get_physical_resource_id(self,attribute=None,**kwargs):
  props=self.props
  key_id=self._get_key_id()
  if not key_id or not props.get("ApiId"):
   return
  return aws_utils.appsync_api_key_arn(props.get("ApiId"),key_id)
 def _get_key_id(self):
  props=self.props
  return props.get("ApiKeyId")or props.get("id")
 def fetch_state(self,stack_name,resources):
  client=aws_stack.connect_to_service("appsync")
  props=self.props
  api_id=props.get("ApiId")
  api_id=self.resolve_refs_recursively(stack_name,api_id,resources)
  keys=client.list_api_keys(apiId=api_id).get("apiKeys",[])
  expires=props.get("expires")or props.get("Expires")
  description=props.get("Description")
  result=[k for k in keys if k.get("description")==description and expires in[None,k.get("expires")]]
  return(result or[None])[0]
 @classmethod
 def get_deploy_templates(cls):
  def _create_params(_,resources,resource_id,**kwargs):
   resource=cls(resources[resource_id])
   res_props=resource.properties
   if not res_props.get("Description"):
    api_id=resource.resolve_refs_recursively(kwargs.get("stack_name"),res_props.get("ApiId"),resources)
    res_props["Description"]=f"Generated API key for AppSync API ID {api_id}"
   if res_props.get("Expires"):
    res_props["Expires"]=int(res_props.get("Expires"))
   result=keys_to_lower(select_attributes(res_props,["ApiId","Description","Expires"]))
   return result
  return{"create":{"function":"create_api_key","parameters":_create_params}}
class AppSyncDataSource(GenericBaseModel):
 @staticmethod
 def cloudformation_type():
  return "AWS::AppSync::DataSource"
 @staticmethod
 def get_deploy_templates():
  def lambda_get_datasource_config(params,**kwargs):
   params=keys_to_lower(clone(params))
   if params.get("dynamoDBConfig"):
    params["dynamodbConfig"]=params.pop("dynamoDBConfig")
   return params
  return{"create":{"function":"create_data_source","parameters":lambda_get_datasource_config}}
 def get_cfn_attribute(self,attribute_name):
  if attribute_name in REF_ARN_ATTRS+["DataSourceArn"]:
   return self.props.get("dataSourceArn")
  if attribute_name=="Name":
   return self.props.get("name")
  return super(AppSyncDataSource,self).get_cfn_attribute(attribute_name)
 def get_physical_resource_id(self,attribute=None,**kwargs):
  return self.props.get("dataSourceArn")
 def fetch_state(self,stack_name,resources):
  props=self.props
  client=aws_stack.connect_to_service("appsync")
  ds_name=props.get("Name")or self.resource_id
  ds_name=self.resolve_refs_recursively(stack_name,ds_name,resources)
  api_id=self.resolve_refs_recursively(stack_name,props.get("ApiId"),resources)
  sources=client.list_data_sources(apiId=api_id)["dataSources"]
  return([s for s in sources if s["name"]==ds_name]or[None])[0]
class AppSyncFunctionConfig(GenericBaseModel):
 @staticmethod
 def cloudformation_type():
  return "AWS::AppSync::FunctionConfiguration"
 def fetch_state(self,stack_name,resources):
  client=aws_stack.connect_to_service("appsync")
  props=self.props
  api_id=self.resolve_refs_recursively(stack_name,props["ApiId"],resources)
  name=self.resolve_refs_recursively(stack_name,props["Name"],resources)
  result=client.list_functions(apiId=api_id).get("functions",[])
  result=[f for f in result if f.get("name")==name]
  return(result or[None])[0]
 def get_cfn_attribute(self,attribute_name):
  props=self.props
  if attribute_name=="FunctionId":
   return props.get("functionArn","").split("functions/")[-1]
  if attribute_name=="FunctionArn":
   return props.get("functionArn")
  if attribute_name=="Name":
   return props.get("name")
  if attribute_name=="DataSourceName":
   return props.get("dataSourceName")
  return super(AppSyncFunctionConfig,self).get_cfn_attribute(attribute_name)
 def get_physical_resource_id(self,attribute,**kwargs):
  return self.props.get("functionArn")
 @staticmethod
 def get_deploy_templates():
  def func_params(params,**kwargs):
   sys_cfg=params.get("SyncConfig")
   if sys_cfg:
    sys_cfg=keys_to_lower(clone(sys_cfg))
   result={"apiId":"ApiId","name":"Name","description":"Description","dataSourceName":"DataSourceName","requestMappingTemplate":"RequestMappingTemplate","responseMappingTemplate":"ResponseMappingTemplate","functionVersion":"FunctionVersion","syncConfig":sys_cfg}
   result={k:params.get(v)for k,v in result.items()if params.get(v)}
   return result
  return{"create":{"function":"create_function","parameters":func_params}}
class GraphQLAPI(GenericBaseModel):
 @staticmethod
 def cloudformation_type():
  return "AWS::AppSync::GraphQLApi"
 def get_cfn_attribute(self,attribute_name):
  props=self.props
  if not props.get("apiId"):
   details=self.fetch_details(props.get("Name"))
   if not details:
    raise Exception('Unable to find GraphQL API named "%s"'%props.get("Name"))
   props["apiId"]=details["apiId"]
  if attribute_name=="ApiId":
   return props.get("apiId")
  if attribute_name in REF_ARN_ATTRS:
   return self.get_physical_resource_id(attribute_name)
  if attribute_name=="GraphQLUrl":
   return appsync_api.get_graphql_url(props["apiId"],use_domain_name=True)
  return super(GraphQLAPI,self).get_cfn_attribute(attribute_name)
 def get_physical_resource_id(self,attribute,**kwargs):
  props=self.props
  return props.get("apiId")and aws_utils.appsync_api_arn(props["apiId"])
 @classmethod
 def fetch_details(cls,api_name):
  client=aws_stack.connect_to_service("appsync")
  apis=client.list_graphql_apis()["graphqlApis"]
  return([a for a in apis if a["name"]==api_name]or[None])[0]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
