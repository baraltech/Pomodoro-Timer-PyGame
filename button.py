import pygame

class Button():
	def __init__(self, surface=None, pos=None, width=None, height=None, text_input=None, font=None, base_color=None, hovering_color=None):
		self.surface = surface
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.width = width
		self.height = height
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.surface is None:
			self.surface = self.text
		else:
			self.surface = pygame.transform.smoothscale(self.surface, (width, height))
		self.rect = self.surface.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.surface is not None:
			screen.blit(self.surface, self.rect)
		screen.blit(self.text, self.text_rect)

	def check_for_input(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def change_color(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)