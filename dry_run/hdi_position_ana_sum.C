/// \file
/// \ingroup tutorial_hist
/// \notebook -js
/// 1-D histogram drawing options.
/// We attach (or generate) the ROOT file in `$ROOTSYS/tutorials/hsimple.root`
/// or `$PWD/hsimple.root`
/// We draw one histogram in different formats.
///
/// \macro_image
/// \macro_code
///
/// \author Rene Brun

#include "TInterpreter.h"
#include "TCanvas.h"
#include "TSystem.h"
#include "TFile.h"
#include "TH2.h"
#include "TNtuple.h"
#include "TPaveLabel.h"
#include "TPaveText.h"
#include "TFrame.h"
#include "TSystem.h"
#include "TInterpreter.h"
#include "data/data_sum.h"

#define DATASIZE 75

void hdi_position_ana_sum()
{

  gStyle->SetPalette(1) ;
  gStyle->SetOptFit(11111111) ;
  gStyle->SetOptStat(1111) ;


  double x0 = 0 ;
  double y0 = 0 ;
  double z0 = 0 ;
  double a0 = 0 ;

  
  auto h1fxx = new TH1F("h1fxx","delta x (um)",10,-50,50);
  auto h1fyy = new TH1F("h1fyy","delta y (um)",10,-50,50);
  auto h1fzz = new TH1F("h1fzz","delta z (um)",10,-100,100);
  auto h1faa = new TH1F("h1faa","angle (degree)",10,-0.10,0.10);
  
  auto h2fxxyy = new TH2F("h2fxxyy","delta y vs delta x",200,-100,100,200,-100,100);

  

  for( int i=0 ; i<DATASIZE ; i++ ){

    x0 += xx[i] ;
    y0 += yy[i] ;
    z0 += zz[i] ;
    a0 += angle[i] ;
  }


  x0 /= (double)DATASIZE ;
  y0 /= (double)DATASIZE ;
  z0 /= (double)DATASIZE ;
  a0 /= (double)DATASIZE ;


  cout << "x0 is : " << x0 << endl ;
  cout << "y0 is : " << y0 << endl ;
  cout << "z0 is : " << z0 << endl ;
  cout << "a0 is : " << a0 << endl ;

  //x0 = 231.750 ;
  //y0 = 397.108 ;
  //z0 = 77.3792 ;
  //a0 = 0.030323 ;
  


  
  for( int i=0 ; i<DATASIZE ; i++ ){
    //std::cout <<  std::setprecision(9) << xx[i] << std::endl ;
    h1fxx->Fill( 1000*(xx[i] - x0) ) ;
    h1fyy->Fill( 1000*(yy[i] - y0) ) ;
    h1fzz->Fill( 1000*(zz[i] - z0) ) ;
    h1faa->Fill( angle[i] ) ;
    h2fxxyy->Fill(  1000*(xx[i] - x0), 1000*(yy[i] - y0) ) ;     
  }

  TF1 *f1xx = new TF1("f1xx","gaus",-0.10, 0.10);
  //h1fxx->Fit("f1xx","L") ;
  TF1 *f1yy = new TF1("f1yy","gaus",-0.10, 0.10);
  //h1fyy->Fit("f1yy","L") ;

  TCanvas *c1 = new TCanvas("c1","MH0115",100,100,1000,1000);
  c1->Divide(2,2) ;
  c1->cd(1) ;
  h1fxx->Draw() ;
  c1->cd(2) ;
  h1fyy->Draw() ;
  c1->cd(3) ;
  //h1fzz->Draw() ;
  //c1->cd(4) ;
  h2fxxyy->SetMarkerStyle(3);
  h2fxxyy->Draw("") ;
  c1->cd(4) ;
  h1faa->Draw() ;

  c1->Print("MH_sum.jpg") ;
  
  
      /*
  TString dir = gROOT->GetTutorialDir();
   dir.Append("/hsimple.C");
   dir.ReplaceAll("/./","/");
   if (gBenchmark->GetBench("hsimple") < 0) gInterpreter->LoadMacro(dir.Data());
   TFile *example = (TFile*)gROOT->ProcessLineFast("hsimple(1)");
   if (!example) return;

   example->ls();
   TH1 *hpx = (TH1*)example->Get("hpx");

   TCanvas *c1 = new TCanvas("c1","Histogram Drawing Options",200,10,700,900);
   TPad *pad1 = new TPad("pad1",
      "The pad with the function",0.03,0.62,0.50,0.92);
   TPad *pad2 = new TPad("pad2",
      "The pad with the histogram",0.51,0.62,0.98,0.92);
   TPad *pad3 = new TPad("pad3",
      "The pad with the histogram",0.03,0.02,0.97,0.57);
   pad1->Draw();
   pad2->Draw();
   pad3->Draw();

   // Draw a global picture title
   TPaveLabel *title = new TPaveLabel(0.1,0.94,0.9,0.98,
                    "Drawing options for one dimensional histograms");
   title->SetTextFont(52);
   title->Draw();

   // Draw histogram hpx in first pad with the default option.
   pad1->cd();
   pad1->GetFrame()->SetFillColor(18);
   hpx->SetFillColor(45);
   hpx->DrawCopy();
   TPaveLabel *label1 = new TPaveLabel(-3.5,700,-1,800,"Default option");
   label1->Draw();

   // Draw hpx as a lego. Clicking on the lego area will show
   // a "transparent cube" to guide you rotating the lego in real time.
   pad2->cd();
   hpx->DrawCopy("lego1");
   TPaveLabel *label2 = new TPaveLabel(-0.72,0.74,-0.22,0.88,"option Lego1");
   label2->Draw();
   TPaveLabel *label2a = new TPaveLabel(-0.93,-1.08,0.25,-0.92,
      "Click on lego to rotate");
   label2a->Draw();

   // Draw hpx with its errors and a marker.
   pad3->cd();
   pad3->SetGridx();
   pad3->SetGridy();
   hpx->SetMarkerStyle(21);
   hpx->Draw("e1p");
   TPaveLabel *label3 = new TPaveLabel(2,600,3.5,650,"option e1p");
   label3->Draw();

   // The following illustrates how to add comments using a PaveText.
   // Attributes of text/lines/boxes added to a PaveText can be modified.
   // The AddText function returns a pointer to the added object.
   TPaveText *pave = new TPaveText(-3.78,500,-1.2,750);
   TText *t1=pave->AddText("You can move");
   t1->SetTextColor(4);
   t1->SetTextSize(0.05);
   pave->AddText("Title and Stats pads");
   pave->AddText("X and Y axis");
   pave->AddText("You can modify bin contents");
   pave->Draw();
   c1->Update();
      */
}
