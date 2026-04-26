"""
Tests automatizados para el sistema de validación de datos
Implementa casos exitosos, de error y edge cases
"""

import pytest
from app.validator import DataValidator


class TestValidacionEmail:
    """Tests para validación de emails"""
    
    def test_email_valido_caso_exitoso(self):
        """Caso exitoso: email con formato correcto"""
        resultado = DataValidator.validar_email("usuario@example.com")
        assert resultado == True, "Debería aceptar email válido"
    
    def test_email_sin_arroba_caso_error(self):
        """Caso de error: email sin arroba"""
        resultado = DataValidator.validar_email("usuarioexample.com")
        assert resultado == False, "Debería rechazar email sin @"
    
    def test_email_vacio_edge_case(self):
        """Edge case: string vacío"""
        resultado = DataValidator.validar_email("")
        assert resultado == False, "Debería rechazar email vacío"


class TestValidacionPassword:
    """Tests para validación de contraseñas"""
    
    def test_password_valida_caso_exitoso(self):
        """Caso exitoso: contraseña cumple todos los requisitos"""
        resultado = DataValidator.validar_password("Password123")
        assert resultado == True, "Debería aceptar contraseña válida"
    
    def test_password_muy_corta_caso_error(self):
        """Caso de error: contraseña con menos de 8 caracteres"""
        resultado = DataValidator.validar_password("Pass1")
        assert resultado == False, "Debería rechazar contraseña corta"
    
    def test_password_limite_edge_case(self):
        """Edge case: contraseña con exactamente 8 caracteres"""
        resultado = DataValidator.validar_password("Pass1234")
        assert resultado == True, "Debería aceptar contraseña en el límite"


class TestValidacionEdad:
    """Tests para validación de edad"""
    
    def test_edad_valida_caso_exitoso(self):
        """Caso exitoso: edad dentro del rango válido"""
        resultado = DataValidator.validar_edad(25)
        assert resultado == True, "Debería aceptar edad válida"
    
    def test_edad_negativa_caso_error(self):
        """Caso de error: edad negativa"""
        resultado = DataValidator.validar_edad(-5)
        assert resultado == False, "Debería rechazar edad negativa"
    
    def test_edad_limite_superior_edge_case(self):
        """Edge case: edad en el límite máximo permitido"""
        resultado = DataValidator.validar_edad(120)
        assert resultado == True, "Debería aceptar edad en el límite superior"