"""
Sistema de validación de datos
Valida emails, contraseñas y edades según reglas de negocio
"""

import re


class DataValidator:
    """Clase para validar diferentes tipos de datos"""
    
    @staticmethod
    def validar_email(email):
        """
        Valida formato de email
        
        Args:
            email (str): Email a validar
            
        Returns:
            bool: True si es válido, False si no
        """
        if not email or not isinstance(email, str):
            return False
        
        # Patrón básico de email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, email))
    
    @staticmethod
    def validar_password(password):
        """
        Valida que la contraseña cumpla requisitos de seguridad:
        - Mínimo 8 caracteres
        - Al menos una mayúscula
        - Al menos una minúscula
        - Al menos un número
        
        Args:
            password (str): Contraseña a validar
            
        Returns:
            bool: True si es válida, False si no
        """
        if not password or not isinstance(password, str):
            return False
        
        if len(password) < 8:
            return False
        
        tiene_mayuscula = any(c.isupper() for c in password)
        tiene_minuscula = any(c.islower() for c in password)
        tiene_numero = any(c.isdigit() for c in password)
        
        return tiene_mayuscula and tiene_minuscula and tiene_numero
    
    @staticmethod
    def validar_edad(edad):
        """
        Valida que la edad esté en un rango válido (0-120)
        
        Args:
            edad (int): Edad a validar
            
        Returns:
            bool: True si es válida, False si no
        """
        if not isinstance(edad, int):
            return False
        
        return 0 <= edad <= 120