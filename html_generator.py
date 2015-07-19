Class HTMLGen:
  ''' Returns html generated code.'''
  pass
  
  def a(self, str_to_html):
      return '<a>' + str_to_html + '</a>'
      
  def b(self, str_to_html):
      return '<b>' + str_to_html + '</b>'
      
  def p(self, str_to_html):
      return '<p>' + str_to_html + '</p>'
      
  def body(self, str_to_html):
      return '<body>' + str_to_html + '</body>'
      
  def div(self, str_to_html):
      return '<div>' + str_to_html + '</div>'
      
  def span(self, str_to_html):
      return '<span>' + str_to_html + '</span>'
      
  def title(self, str_to_html):
      return '<title>' + str_to_html + '</title>'
      
  def comment(self, str_to_html):
      return '<!--' + str_to_html + '-->'
            
