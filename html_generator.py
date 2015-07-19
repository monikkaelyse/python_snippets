Class HTMLGen:
  ''' HTML code generator. '''

  def open_bracket(self, html_tag):
      return '<{}>'.format(html_tag)
  def close_bracket(self, html_tag):
      return '</{}>'.format(html_tag)
  def generate_html(self, to_html, html_tag):
      return '{0}{1}{2}'.format(self.open_bracket(html_tag), to_html, self.close_bracket(html_tag))
      
  def a(self, to_html):
      return self.generate_html(to_html, 'a')
  def b(self, to_html):
      return self.generate_html(to_html, 'b')    
  def p(self, to_html):
      return self.generate_html(to_html, 'p')
  def body(self, to_html):
      return self.generate_html(to_html, 'body')
  def div(self, to_html):
      return self.generate_html(to_html, 'div')    
  def span(self, to_html):
      return self.generate_html(to_html, 'span')
  def title(self, to_html):
      return self.generate_html(to_html, 'title')    
  def comment(self, to_html):
      return '<!--{}-->'.format(to_html)lass HTMLGen:
  ''' Returns html generated code.'''
  pass
  
            
