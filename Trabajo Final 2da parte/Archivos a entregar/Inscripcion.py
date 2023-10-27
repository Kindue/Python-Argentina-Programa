######################### INSCRIPCION #########################
#Modela una inscripcion para un examen, contiene consultas triviales
#para obtener y modificar sus atributos los cuales son:
#fecha, nombre del alumno, nombre de la materia, nombre del profesor
#curso, division y nota

class Inscripcion:
	def __init__(self, fecha, alumno, materia, profesor, curso, division, nota=0):
		self._fecha = fecha
		self._alumno = alumno
		self._materia = materia
		self._profesor = profesor
		self._curso = curso
		self._division = division
		self._nota = nota

	def getFecha(self):
		return self._fecha

	def getAlumno(self):
		return self._alumno

	def getMateria(self):
		return self._materia

	def getProfesor(self):
		return self._profesor

	def getCurso(self):
		return self._curso

	def getDivision(self):
		return self._division

	def getNota(self):
		return self._nota

	def setFecha(self, nuevaFecha):
		self._fecha = nuevaFecha

	def setAlumno(self, nuevoAlumno):
		self._alumno = nuevoAlumno

	def setMateria(self, nuevaMateria):
		self._materia = nuevaMateria

	def setProfesor(self, nuevoProfesor):
		self._profesor = nuevoProfesor

	def setCurso(self, nuevoCurso):
		self._curso = nuevoCurso

	def setDivision(self, nuevaDivision):
		self._division = nuevaDivision

	def setNota(self, nuevaNota):
		self._nota = nuevaNota

	def __str__(self):
		return f"{self._fecha},{self._alumno},{self._materia},{self._profesor},{self._curso},{self._division},{self._nota}"