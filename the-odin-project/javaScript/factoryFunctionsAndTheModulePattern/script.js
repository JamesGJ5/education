const alien = (englishName, galaxyOfOrgin) => {
    const translatedName = englishName + '-' + englishName;
    const sayHello = (name) => console.log(`Hello, my name is ${ name } and I am 
        from ${galaxyOfOrgin}!`);
    return {sayHello};
}