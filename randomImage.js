// SOURCE: https://gist.github.com/AstDerek/5841966

var _landingpageImageWidth = null;
(function($){
        $.randomImage = {
            defaults: {
                //you can change these defaults to your own preferences.
                path: 'img/', //change this to the path of your images
                myImages: ['river.jpg', 'the-narrows.jpg', 'ocean.jpg' ] //put image names in this bracket. ex: 'harold.jpg', 'maude.jpg', 'etc'
            }
        };
        
       
       
        $.fn.extend({
        	
            randomImage:function(config) {
                var config = $.extend({}, $.randomImage.defaults, config);
                
                return this.each(function() {
                    var imageNames = config.myImages,
                    //get size of array, randomize a number from this
                    // use this number as the array index
                    imageNamesSize = imageNames.length,
                    lotteryNumber = Math.floor(Math.random()*imageNamesSize),
                    winnerImage = imageNames[lotteryNumber],
                    fullPath = config.path + winnerImage;
                    
                    //put this image into DOM at class of randomImage
                    // alt tag will be image filename.
                    $(this).attr({
                        src: fullPath,
                        alt: winnerImage
                    });
                    //$("#loaderImage").css("display","none");
                    
                    var myImage = new Image();
					myImage.name = winnerImage;
					myImage.onload = getWidthAndHeight;
					myImage.src = fullPath;
					
					  
					  function getWidthAndHeight() {
					  	_landingpageImageWidth = this.width;
					    //alert("'" + this.name + "' is " + this.width + " by " + this.height + " pixels in size.");
					    return true;
					}
                      
                });
                
                
                
        
            }
            
        });
         
    }(jQuery));
    