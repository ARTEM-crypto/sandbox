params.(:phone, :description, :userSystem, :userScreen).update(parsed_response)

{}.tap do |h|
  h[:phone] = params[:phone]
  h[:description] = params[:description]
  h[:userSystem] = params[:userSystem]
  h[:userScreen] = params[:userScreen]
end
