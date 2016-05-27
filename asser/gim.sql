CREATE TABLE AsiganacionRutina (
  idAsiganacionRutina INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Cliente_id INTEGER UNSIGNED NOT NULL,
  Rutina_idRutina INTEGER UNSIGNED NOT NULL,
  estado BOOL NULL,
  fecha DATE NULL,
  PRIMARY KEY(idAsiganacionRutina),
  INDEX AsiganacionRutina_FKIndex1(Rutina_idRutina),
  INDEX AsiganacionRutina_FKIndex2(Cliente_id)
);

CREATE TABLE AsigancionEntrenamiento (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  AsiganacionRutina_idAsiganacionRutina INTEGER UNSIGNED NOT NULL,
  Entrenamiento_id INTEGER UNSIGNED NOT NULL,
  estado BOOL NULL,
  PRIMARY KEY(id),
  INDEX AsigancionEntrenamiento_FKIndex1(Entrenamiento_id),
  INDEX AsigancionEntrenamiento_FKIndex2(AsiganacionRutina_idAsiganacionRutina)
);

CREATE TABLE AsignacionEjercicio (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  AsigancionEntrenamiento_id INTEGER UNSIGNED NOT NULL,
  Entrenamiento_has_Eejercicio_Ejercicio_id INTEGER UNSIGNED NOT NULL,
  Entrenamiento_has_Eejercicio_Entrenamiento_id INTEGER UNSIGNED NOT NULL,
  estado BOOL NULL,
  repeticiones INTEGER UNSIGNED NULL,
  series INTEGER UNSIGNED NULL,
  PRIMARY KEY(id),
  INDEX AsignacionEjercicio_FKIndex1(Entrenamiento_has_Eejercicio_Entrenamiento_id, Entrenamiento_has_Eejercicio_Ejercicio_id),
  INDEX AsignacionEjercicio_FKIndex2(AsigancionEntrenamiento_id)
);

CREATE TABLE Asistencia (
  idAsistencia INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  AsiganacionRutina_idAsiganacionRutina INTEGER UNSIGNED NOT NULL,
  Cliente_id INTEGER UNSIGNED NOT NULL,
  TipoPago_id INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(idAsistencia),
  INDEX Asistencia_FKIndex1(TipoPago_id),
  INDEX Asistencia_FKIndex2(Cliente_id),
  INDEX Asistencia_FKIndex3(AsiganacionRutina_idAsiganacionRutina)
);

CREATE TABLE Cliente (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  cedula VARCHAR NULL,
  Nombre VARCHAR NULL,
  apellidos VARCHAR NULL,
  direccion VARCHAR NULL,
  telefono VARCHAR NULL,
  dias INTEGER UNSIGNED NULL,
  PRIMARY KEY(id)
);

CREATE TABLE Compra (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Cliente_id INTEGER UNSIGNED NOT NULL,
  Menudeo_id INTEGER UNSIGNED NOT NULL,
  cantidad FLOAT NULL,
  precio FLOAT NULL,
  Estado INTEGER UNSIGNED NULL,
  PRIMARY KEY(id),
  INDEX Venta_FKIndex1(Menudeo_id),
  INDEX Compra_FKIndex2(Cliente_id)
);

CREATE TABLE Ejercicio (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre VARCHAR NULL,
  descripcion VARCHAR NULL,
  estado BOOL NULL,
  PRIMARY KEY(id)
);

CREATE TABLE Entrenamiento (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Musculo_id INTEGER UNSIGNED NOT NULL,
  nombre INTEGER UNSIGNED NULL,
  estado INTEGER UNSIGNED NULL,
  PRIMARY KEY(id),
  INDEX Entrenamiento_FKIndex1(Musculo_id)
);

CREATE TABLE Entrenamiento_has_Eejercicio (
  Entrenamiento_id INTEGER UNSIGNED NOT NULL,
  Ejercicio_id INTEGER UNSIGNED NOT NULL,
  serie INTEGER UNSIGNED NULL,
  repeticiones INTEGER UNSIGNED NULL,
  estado INTEGER UNSIGNED NULL,
  PRIMARY KEY(Entrenamiento_id, Ejercicio_id),
  INDEX Entrenamiento_has_Eejercicio_FKIndex1(Entrenamiento_id),
  INDEX Entrenamiento_has_Eejercicio_FKIndex2(Ejercicio_id)
);

CREATE TABLE Medidas (
  idMedidas INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Cliente_id INTEGER UNSIGNED NOT NULL,
  peso FLOAT NULL,
  cuello FLOAT NULL,
  hombros FLOAT NULL,
  pecho FLOAT NULL,
  biceps FLOAT NULL,
  antebrazo FLOAT NULL,
  Cintura FLOAT NULL,
  murlo_superior FLOAT NULL,
  murlo_centro FLOAT NULL,
  murlo_inferior FLOAT NULL,
  gemelo_izq FLOAT NULL,
  gemolo_derecho FLOAT NULL,
  PRIMARY KEY(idMedidas),
  INDEX Medidas_FKIndex1(Cliente_id)
);

CREATE TABLE Menudeo (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Producto_id INTEGER UNSIGNED NOT NULL,
  estado BOOL NULL,
  precio FLOAT NULL,
  PRIMARY KEY(id),
  INDEX Menudeo_FKIndex1(Producto_id)
);

CREATE TABLE Musculo (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre VARCHAR NULL,
  estado BOOL NULL,
  PRIMARY KEY(id)
);

CREATE TABLE Pago (
  idPago INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Cliente_id INTEGER UNSIGNED NOT NULL,
  TipoPago_id INTEGER UNSIGNED NOT NULL,
  estado BOOL NULL,
  valor FLOAT NULL,
  fecha_realizacion DATE NULL,
  fecha_fin DATE NULL,
  PRIMARY KEY(idPago),
  INDEX Pago_FKIndex1(TipoPago_id),
  INDEX Pago_FKIndex2(Cliente_id)
);

CREATE TABLE Producto (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre INTEGER UNSIGNED NULL,
  precio FLOAT NULL,
  cantidad FLOAT NULL,
  existencias INTEGER UNSIGNED NULL,
  estado BOOL NULL,
  PRIMARY KEY(id)
);

CREATE TABLE Rutina (
  idRutina INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre VARCHAR NULL,
  estado BOOL NULL,
  PRIMARY KEY(idRutina)
);

CREATE TABLE Rutina_has_Entrenamiento (
  Rutina_idRutina INTEGER UNSIGNED NOT NULL,
  Entrenamiento_id INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(Rutina_idRutina, Entrenamiento_id),
  INDEX Rutina_has_Entrenamiento_FKIndex1(Rutina_idRutina),
  INDEX Rutina_has_Entrenamiento_FKIndex2(Entrenamiento_id)
);

CREATE TABLE TipoPago (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre INTEGER UNSIGNED NULL,
  valor INTEGER UNSIGNED NULL,
  estado BOOL NULL,
  descripcion VARCHAR NULL,
  PRIMARY KEY(id)
);


