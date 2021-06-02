public class Janela extends Canvas implements Runnable{
   
    int[] pixelsFundo;
    private BufferedImage img;
    private int[][] mapa = new int[][]{ {0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},    
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                                        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}};
    private int jogadorX = 11;
    private int jogadorY = 11;
   
    public Janela()
    {
        this.img = new BufferedImage(800, 600, BufferedImage.TYPE_INT_RGB);
        this.pixelsFundo = ((DataBufferInt)img.getRaster().getDataBuffer()).getData();
    }
    public void render(int x, int y, int xPos, int yPos)
    {
        BufferStrategy bs = this.getBufferStrategy();
        if(bs == null)
        {
            this.createBufferStrategy(2);
            bs = this.getBufferStrategy();
        }
       
        Graphics g = bs.getDrawGraphics();
        g.drawRect(xPos,yPos,x, y);
        g.dispose();
        bs.show();
    }
    public void calcular()
    {
        int poxX = 0;
        for (int i = 0; i < mapa.length; i++)
        {
            poxX = 0;
            for(int j = 0; j < mapa.length; j++)
            {
                if(mapa[i][j] == 2)
                {
                    double catetoAdj = this.jogadorX - i;
                    double catetoOp = this.jogadorY - j;
                    double hipotenusa = catetoOp / catetoAdj;
                   
                    if(hipotenusa < 0)
                    {
                        hipotenusa = hipotenusa * -1;
                    }
                    System.out.println(hipotenusa);
                    render(37, (int)(200-(hipotenusa*50)),poxX, (int)(180+((hipotenusa*50)/2)));
                }
                poxX += 37;
            }
        }
    }