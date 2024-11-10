from VALIDACIONES.Validaciones import validacion_dig, validacionmail, validar_mayus_nombre, validar_nota, validar_num, validar_contraseña

def test_validacion_dig():
    # def validacion_dig(texto, numero_opciones)
    assert validacion_dig("5", 6) == True
    assert validacion_dig("6", 5) == False

def test_validacionmail():
    # def validacionmail (mail)
    assert validacionmail("roberto@sistem.edu.ar") == True
    assert validacionmail("roberto@uade.edu.ar") == False
    assert validacionmail("ro@sistem.edu.ar") == False

def test_validar_mayus_nombre():
    # def validar_mayus_nombre (nombre)
    assert validar_mayus_nombre("Cheng Li") == True
    assert validar_mayus_nombre("Felipe daquino") == False

def test_validar_nota():
    # def validar_nota (nota)
    assert validar_nota("3") == True
    assert validar_nota("3.1") == True
    assert validar_nota("10.0") == True
    assert validar_nota("0") == False
    assert validar_nota("10.2") == False
    assert validar_nota("20") == False

def test_validar_num():
    # def validar_num(car)
    assert validar_num("32135") == True
    assert validar_num("31a23") == False
    assert validar_num(":3123") == False
    assert validar_num("(3123)") == False

def test_validar_contraseña():
    # def validar_contraseña(contraseña)
    assert validar_contraseña("Pepito123123") == True
    assert validar_contraseña("pePito123123") == True
    assert validar_contraseña("123123pEpito") == True
    assert validar_contraseña("   Pepito123123   ") == False
    assert validar_contraseña("pepito123123") == False
    assert validar_contraseña("Pepi123") == False
