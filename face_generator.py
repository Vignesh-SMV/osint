def face():

    def banner():
        print("""
            	 ''~``
                                        ( o o )
                +------------------.oooO--(_)--Oooo.------------------+
                |                                                     |
                |           TEMPORARY FACE GENERATION TOOL            |
                |                    [21BIT049]                       |
                |                                                     |
                |                    .oooO                            |
                |                    (   )   Oooo.                    |
                +---------------------\ (----(   )--------------------+
                                       \_)    ) /
                                             (_/

            	=[===> 21BIT049 | https://github.com/Vignesh-SMV <===]= """)

    banner()


    import tensorflow as tf
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    generator = tf.keras.models.load_model("C:\\Users\\gowrishankar\\Downloads\\generator.h5")



    def generate_and_visualize_images(generator, num_images=16, save_path="C:\\Users\\gowrishankar\\Desktop\\img"):
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        noise = np.random.normal(0, 1, size=[num_images, 100])
        generated_images = generator.predict(noise)
        generated_images = 0.5 * generated_images + 0.5  # Rescale to [0, 1]

        plt.figure(figsize=(10, 10))
        for i in range(num_images):
            plt.subplot(3, 3, i + 1)
            plt.imshow(generated_images[i])
            plt.axis('off')

            image_filename = os.path.join(save_path, f"generated_image_{i}.png")
            plt.imsave(image_filename, generated_images[i])


        #plt.tight_layout()
        plt.show()


    generate_and_visualize_images(generator, num_images=2)

