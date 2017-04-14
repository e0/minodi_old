const generate = () => {
  return {
    strong1: getRandomStrongColor(),
    strong2: getRandomStrongColor(),
    pastel1: getRandomPastelColor(),
    pastel2: getRandomPastelColor()
  }
}

const getRandomStrongColor = () => {
  return getRandomColor('strong')
}

const getRandomPastelColor = () => {
  return getRandomColor('pastel')
}

const getRandomColor = (type) => {
  const funk = type === 'pastel' ? getRandomPastelPart : getRandomStrongPart

  return `rgb(${funk()}, ${funk()}, ${funk()})`
}

const getRandomStrongPart = () => {
  return getRandomInt(42, 77)
}

const getRandomPastelPart = () => {
  return getRandomInt(142, 177)
}

const getRandomInt = (min, max) => {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min)) + min
}

export default generate
